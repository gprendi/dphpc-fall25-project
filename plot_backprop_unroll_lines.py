#!/usr/bin/env python3

import argparse
import re
import warnings
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd

import plot_backprop_results as pbr
from npbench.infrastructure import utilities as util


def _discover_dbs(pattern: str) -> List[Path]:
    paths = [Path(p) for p in sorted(Path().glob(pattern))]
    return [p for p in paths if p.is_file()]


def _unroll_label(db_path: Path) -> str:
    stem = db_path.stem
    prefix = "npbench-unroll-"
    if stem.startswith(prefix):
        return stem[len(prefix):]
    return stem


def _sort_key(label: str) -> Tuple[int, object]:
    """Sort numeric labels naturally, otherwise lexicographically."""
    if re.fullmatch(r"\d+", label):
        return (0, int(label))
    if re.fullmatch(r"\d+\.\d+", label):
        return (0, float(label))
    return (1, label)


def _as_float(label: str) -> Optional[float]:
    if re.fullmatch(r"\d+", label):
        return float(int(label))
    if re.fullmatch(r"\d+\.\d+", label):
        return float(label)
    return None


def _infer_preset_from_name(name: str) -> Optional[str]:
    """Infer NPBench preset from a folder label like 'unroll-go_fast-M'."""
    parts = re.split(r"[-_]+", name)
    if not parts:
        return None
    last = parts[-1]
    if last in {"S", "M", "L", "paper"}:
        return last
    return None


def _load_benchmark_aliases(bench_dir: Path) -> Dict[str, str]:
    """Map user-facing benchmark IDs to the DB 'benchmark' values.

    In this project the SQLite 'results.benchmark' typically stores the
    benchmark short_name (e.g. 'npgofast'), while humans often refer to the
    bench by its metadata file stem (e.g. 'go_fast').
    """
    aliases: Dict[str, str] = {}
    for path in sorted(bench_dir.glob("*.json")):
        try:
            payload = path.read_text()
        except OSError:
            continue
        try:
            import json

            parsed = json.loads(payload)
        except Exception:
            continue
        bench = parsed.get("benchmark", {}) if isinstance(parsed, dict) else {}
        short_name = bench.get("short_name")
        if not short_name:
            continue
        stem = path.stem
        aliases[stem] = short_name
        aliases[short_name] = short_name
    return aliases


def _resolve_benchmark_args(
    requested: Optional[List[str]],
    bench_dir: Path,
) -> Optional[List[str]]:
    if not requested:
        return None
    aliases = _load_benchmark_aliases(bench_dir)
    resolved: List[str] = []
    for name in requested:
        canon = aliases.get(name, name)
        resolved.append(canon)
    return resolved


def fetch_results_from_db(db_file: Path, preset: str, frameworks: List[str]) -> pd.DataFrame:
    conn = util.create_connection(str(db_file))
    if conn is None:
        raise RuntimeError(f"Failed to open DB: {db_file}")

    data = pd.read_sql_query(
        """
        SELECT benchmark, domain, framework, mode, details, time
        FROM results
        WHERE preset = ?
          AND mode IN ('forward', 'backward')
        """,
        conn,
        params=(preset,),
    )
    data = data[data["domain"] != ""]
    data = data[data["framework"].isin(frameworks)].reset_index(drop=True)
    return data


def _load_medians_for_unroll_dbs(
    dbs: List[Path],
    preset: str,
    framework: str,
) -> Dict[str, pd.DataFrame]:
    per_db_medians: Dict[str, pd.DataFrame] = {}
    for db in dbs:
        label = _unroll_label(db)
        try:
            raw = fetch_results_from_db(db, preset, [framework])
        except Exception as exc:
            warnings.warn(f"Skipping DB {db}: {exc}", RuntimeWarning, stacklevel=2)
            continue
        if raw.empty:
            warnings.warn(
                f"No rows for framework={framework!r}, preset={preset!r} in {db}",
                RuntimeWarning,
                stacklevel=2,
            )
            continue

        medians, _filtered = pbr.select_best_runs(raw)
        per_db_medians[label] = medians
    return per_db_medians


def _ordered_benchmarks_from_all(
    per_db_medians: Dict[str, pd.DataFrame],
    labels: Dict[str, str],
) -> List[str]:
    benches: set[str] = set()
    for med in per_db_medians.values():
        benches |= set(med["benchmark"].unique())
    ordered = sorted(benches)
    ordered.sort(key=lambda b: labels.get(b, b))
    return ordered


def plot_unroll_lines(
    per_db_medians: Dict[str, pd.DataFrame],
    labels: Dict[str, str],
    framework: str,
    mode: str,
    preset: str,
    output_path: Path,
    use_logscale: bool,
    relative_to_first: bool,
    speedup: bool,
    only_benchmarks: Optional[List[str]] = None,
) -> None:
    benches = _ordered_benchmarks_from_all(per_db_medians, labels)
    if only_benchmarks:
        benches = [b for b in benches if b in set(only_benchmarks)]

    if not benches:
        raise SystemExit("No benchmarks to plot after filtering.")

    # Build a (unroll -> benchmark -> time_ms) table.
    unroll_labels = sorted(per_db_medians.keys(), key=_sort_key)
    unroll_x: List[float] = []
    keep_labels: List[str] = []
    for label in unroll_labels:
        x = _as_float(label)
        if x is None:
            warnings.warn(
                f"Skipping non-numeric unroll label {label!r} (derived from DB name)",
                RuntimeWarning,
                stacklevel=2,
            )
            continue
        unroll_x.append(x)
        keep_labels.append(label)

    if not unroll_x:
        raise SystemExit(
            "No numeric unroll labels found. Expected DB names like npbench-unroll-16.db"
        )

    fig, ax = plt.subplots(figsize=(max(10, len(unroll_x) * 0.55), 6))

    # One line per benchmark (y = median runtime for this benchmark at each unroll).
    for bench in benches:
        ys: List[float] = []
        for label in keep_labels:
            med = per_db_medians[label]
            subset = med[(med["framework"] == framework) & (med["mode"] == mode)]
            val = subset[subset["benchmark"] == bench]["time_ms"]
            ys.append(float(val.iloc[0]) if not val.empty else np.nan)

        if relative_to_first:
            baseline = ys[0] if ys else np.nan
            if baseline and not np.isnan(baseline) and baseline > 0:
                arr = np.asarray(ys, dtype=float)
                if speedup:
                    ys = (float(baseline) / arr).tolist()
                else:
                    ys = (arr / float(baseline)).tolist()
            else:
                warnings.warn(
                    f"Cannot normalize benchmark {bench!r}: missing/invalid baseline at first unroll.",
                    RuntimeWarning,
                    stacklevel=2,
                )
        ax.plot(
            unroll_x,
            ys,
            marker="o",
            linewidth=1.8,
            markersize=4,
            label=labels.get(bench, bench),
        )

    ax.set_title(
        (
            f"{framework} {mode} median runtime vs unroll (preset={preset})"
            if not relative_to_first
            else (
                f"{framework} {mode} speedup vs unroll (preset={preset})"
                if speedup
                else f"{framework} {mode} runtime scale vs unroll (preset={preset})"
            )
        )
    )
    ax.set_xlabel("Unroll factor")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (× vs first unroll)" if speedup else "Runtime scale (× first unroll)")
    )

    ax.set_xscale("log", base=2)
    ax.set_xticks(unroll_x)
    ax.set_xticklabels([str(int(x)) if float(x).is_integer() else str(x) for x in unroll_x])
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=2, subs="auto"))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())

    if use_logscale:
        ax.set_yscale("log")

    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.grid(axis="y", which="major", linestyle="--", alpha=0.4)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.25)
    ax.legend(title="benchmark", ncol=2)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def plot_unroll_lines_series(
    series_to_per_db_medians: Dict[str, Dict[str, pd.DataFrame]],
    labels: Dict[str, str],
    framework: str,
    mode: str,
    output_path: Path,
    use_logscale: bool,
    relative_to_first: bool,
    speedup: bool,
    only_benchmarks: Optional[List[str]] = None,
    bench: Optional[str] = None,
) -> None:
    """Plot median runtime vs unroll with one line per series (directory).

    If `bench` is provided, plot only that benchmark. Otherwise plot all
    (or `only_benchmarks` if provided) as separate figures in the caller.
    """

    # Determine benchmark list from the union across all series.
    all_medians: Dict[str, pd.DataFrame] = {}
    for _series, per_db in series_to_per_db_medians.items():
        for _lbl, med in per_db.items():
            all_medians[f"{_series}:{_lbl}"] = med
    benches = _ordered_benchmarks_from_all(all_medians, labels)
    if only_benchmarks:
        benches = [b for b in benches if b in set(only_benchmarks)]
    if bench is not None:
        benches = [b for b in benches if b == bench]
    if not benches:
        raise SystemExit("No benchmarks to plot after filtering.")

    if len(benches) != 1:
        raise SystemExit(
            "Multiple-series plotting expects exactly one benchmark. "
            "Pass --benchmarks <one_benchmark>."
        )
    bench = benches[0]

    fig, ax = plt.subplots(figsize=(10, 6))

    for series_label in sorted(series_to_per_db_medians.keys()):
        per_db = series_to_per_db_medians[series_label]
        unroll_labels = sorted(per_db.keys(), key=_sort_key)

        xs: List[float] = []
        ys: List[float] = []
        for label in unroll_labels:
            x = _as_float(label)
            if x is None:
                continue
            med = per_db[label]
            subset = med[(med["framework"] == framework) & (med["mode"] == mode)]
            val = subset[subset["benchmark"] == bench]["time_ms"]
            xs.append(x)
            ys.append(float(val.iloc[0]) if not val.empty else np.nan)

        if relative_to_first and ys:
            baseline = ys[0]
            if baseline and not np.isnan(baseline) and baseline > 0:
                arr = np.asarray(ys, dtype=float)
                if speedup:
                    ys = (float(baseline) / arr).tolist()
                else:
                    ys = (arr / float(baseline)).tolist()
            else:
                warnings.warn(
                    f"Cannot normalize series {series_label!r}: missing/invalid baseline at first unroll.",
                    RuntimeWarning,
                    stacklevel=2,
                )

        if not xs:
            warnings.warn(
                f"Series {series_label!r} had no numeric unroll labels.",
                RuntimeWarning,
                stacklevel=2,
            )
            continue
        ax.plot(xs, ys, marker="o", linewidth=1.8, markersize=4, label=series_label)

    ax.set_title(
        (
            f"{framework} {mode} median runtime vs unroll ({labels.get(bench, bench)})"
            if not relative_to_first
            else (
                f"{framework} {mode} speedup vs unroll ({labels.get(bench, bench)})"
                if speedup
                else f"{framework} {mode} runtime scale vs unroll ({labels.get(bench, bench)})"
            )
        )
    )
    ax.set_xlabel("Unroll factor")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (× vs first unroll)" if speedup else "Runtime scale (× first unroll)")
    )
    ax.set_xscale("log", base=2)
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=2, subs="auto"))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())

    if use_logscale:
        ax.set_yscale("log")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.grid(axis="y", which="major", linestyle="--", alpha=0.4)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.25)
    ax.legend(title="series")
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read multiple npbench-unroll-*.db files (same schema as npbench.db) "
            "and create a line plot with one line per DB."
        )
    )
    parser.add_argument(
        "--db-glob",
        default="npbench-unroll-*.db",
        help="Glob pattern to discover unroll DB files.",
    )
    parser.add_argument(
        "--db-dirs",
        nargs="+",
        default=None,
        help=(
            "One or more directories, each containing npbench-unroll-*.db. "
            "When provided, plots one line per directory (series)."
        ),
    )
    parser.add_argument(
        "--series-presets",
        nargs="+",
        default=None,
        help=(
            "Optional presets (S/M/L/paper), one per --db-dirs entry. "
            "If omitted, tries to infer from directory name (e.g. ...-M)."
        ),
    )
    parser.add_argument(
        "-p",
        "--preset",
        choices=["S", "M", "L", "paper"],
        default="S",
        help="Benchmark preset to plot.",
    )
    parser.add_argument(
        "--framework",
        default="pytorch_cpu",
        help="Framework to plot (single framework).",
    )
    parser.add_argument(
        "--mode",
        choices=["forward", "backward"],
        default="backward",
        help="Execution mode to plot.",
    )
    parser.add_argument(
        "--benchmarks",
        nargs="+",
        default=None,
        help=(
            "Optional list of benchmarks to include. Accepts either bench_info IDs "
            "(e.g. go_fast) or stored short_names (e.g. npgofast)."
        ),
    )
    parser.add_argument(
        "--logy",
        action="store_true",
        help="Use log scale for the y-axis.",
    )
    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Plot absolute runtimes in ms instead of normalizing to the first unroll point.",
    )
    parser.add_argument(
        "--runtime-scale",
        action="store_true",
        help=(
            "When normalizing (default), plot runtime scale (runtime / first) instead of speedup (first / runtime)."
        ),
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="ad_plots",
        help="Directory for generated figures.",
    )
    parser.add_argument(
        "--results-subdir",
        "-r",
        default=pbr.default_results_subdir_name(datetime.now()),
        help="Subfolder under --output-dir for the generated figure.",
    )
    parser.add_argument(
        "--bench-info-dir",
        default="bench_info",
        help="Directory containing benchmark metadata JSON files.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    multi_series = args.db_dirs is not None

    output_dir = Path(args.output_dir) / args.results_subdir
    output_dir.mkdir(parents=True, exist_ok=True)

    bench_dir = Path(args.bench_info_dir)
    labels = pbr.load_benchmark_labels(bench_dir)
    resolved_benchmarks = _resolve_benchmark_args(args.benchmarks, bench_dir)

    if multi_series:
        db_dirs = [Path(d) for d in args.db_dirs]
        for d in db_dirs:
            if not d.is_dir():
                raise SystemExit(f"Not a directory: {d}")
        series_presets: List[Optional[str]]
        if args.series_presets is not None:
            if len(args.series_presets) != len(db_dirs):
                raise SystemExit("--series-presets must match the length of --db-dirs")
            series_presets = list(args.series_presets)
        else:
            series_presets = [None] * len(db_dirs)

        series_to_per_db_medians: Dict[str, Dict[str, pd.DataFrame]] = {}
        for d, preset_override in zip(db_dirs, series_presets):
            inferred = _infer_preset_from_name(d.name)
            preset = preset_override or inferred or args.preset
            dbs = sorted(d.glob("npbench-unroll-*.db"))
            if not dbs:
                warnings.warn(
                    f"No DBs found in {d} matching npbench-unroll-*.db",
                    RuntimeWarning,
                    stacklevel=1,
                )
                continue
            per_db_medians = _load_medians_for_unroll_dbs(dbs, preset, args.framework)
            if per_db_medians:
                series_to_per_db_medians[f"{d.name} ({preset})"] = per_db_medians

        if not series_to_per_db_medians:
            raise SystemExit("No usable DBs found across --db-dirs; nothing to plot.")

        bench_tag = (
            resolved_benchmarks[0]
            if resolved_benchmarks and len(resolved_benchmarks) == 1
            else ""
        )
        out_name = f"backprop_unroll_lines_{args.framework}_{args.mode}_{bench_tag or 'one_bench'}_series.png"
        output_path = output_dir / out_name
        plot_unroll_lines_series(
            series_to_per_db_medians,
            labels,
            framework=args.framework,
            mode=args.mode,
            output_path=output_path,
            use_logscale=args.logy,
            relative_to_first=(not args.absolute),
            speedup=(not args.runtime_scale),
            only_benchmarks=resolved_benchmarks,
        )
    else:
        dbs = _discover_dbs(args.db_glob)
        if not dbs:
            raise SystemExit(f"No DBs matched --db-glob={args.db_glob!r}")
        per_db_medians = _load_medians_for_unroll_dbs(dbs, args.preset, args.framework)
        if not per_db_medians:
            raise SystemExit("No usable DBs produced data; nothing to plot.")

        out_name = f"backprop_unroll_lines_{args.framework}_{args.mode}_{args.preset}.png"
        output_path = output_dir / out_name
        plot_unroll_lines(
            per_db_medians,
            labels,
            framework=args.framework,
            mode=args.mode,
            preset=args.preset,
            output_path=output_path,
            use_logscale=args.logy,
            relative_to_first=(not args.absolute),
            speedup=(not args.runtime_scale),
            only_benchmarks=resolved_benchmarks,
        )

    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
