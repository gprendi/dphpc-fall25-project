#!/usr/bin/env python3

import argparse
import re
import warnings
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
from matplotlib import font_manager, ticker
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

import plot_backprop_results as pbr
from npbench.infrastructure import utilities as util


def _discover_dbs(pattern: str) -> List[Path]:
    paths = [Path(p) for p in sorted(Path().glob(pattern))]
    return [p for p in paths if p.is_file()]


def _unroll_label(db_path: Path) -> str:
    stem = db_path.stem
    if stem == "npbench-baseline":
        # Treat baseline DBs as unroll factor 1.
        return "1"
    if stem == "npbench-noncompiled":
        # Special DB: same workload, but noncompiled implementation.
        # Keep non-numeric so it won't be treated as an x point.
        return "noncompiled"
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


def _font_size_points(size: object, default: float = 10.0) -> float:
    """Convert a Matplotlib font size (number or named size) to points."""
    try:
        return float(size)  # type: ignore[arg-type]
    except Exception:
        try:
            return float(font_manager.FontProperties(size=size).get_size_in_points())
        except Exception:
            return float(default)


def _apply_uniform_font(ax: plt.Axes, size_pt: float) -> None:
    ax.tick_params(axis="both", which="both", labelsize=size_pt)
    ax.xaxis.label.set_size(size_pt)
    ax.yaxis.label.set_size(size_pt)
    ax.title.set_size(size_pt)
    leg = ax.get_legend()
    if leg is not None:
        for txt in leg.get_texts():
            txt.set_fontsize(size_pt)
        if leg.get_title() is not None:
            leg.get_title().set_fontsize(size_pt)


def _set_speedup_power2_yticks(ax: plt.Axes, ys: np.ndarray) -> None:
    """For speedup plots on a log y-axis, label powers of 2 explicitly."""
    finite = ys[np.isfinite(ys) & (ys > 0)]
    if finite.size == 0:
        return
    lo = float(np.nanmin(finite))
    hi = float(np.nanmax(finite))
    if not (lo > 0 and hi > 0):
        return
    exp_lo = int(np.floor(np.log2(lo)))
    exp_hi = int(np.ceil(np.log2(hi)))
    # Cap to avoid pathological tick explosions.
    exp_hi = min(exp_hi, exp_lo + 60)

    # Match the x-axis style: label as 2^k (and keep it readable by stepping by 2).
    start = exp_lo if (exp_lo % 2 == 0) else (exp_lo - 1)
    end = exp_hi if (exp_hi % 2 == 0) else (exp_hi + 1)
    ticks = [2**e for e in range(start, end + 1, 2)]

    ax.set_yscale("log", base=2)
    ax.set_yticks(ticks)
    ax.set_yticklabels([rf"$2^{{{e}}}$" for e in range(start, end + 1, 2)])
    ax.yaxis.set_minor_locator(ticker.LogLocator(base=2, subs="auto"))
    ax.yaxis.set_minor_formatter(ticker.NullFormatter())


def _infer_preset_from_name(name: str) -> Optional[str]:
    """Infer NPBench preset from a folder label like 'unroll-go_fast-M'."""
    parts = re.split(r"[-_]+", name)
    if not parts:
        return None
    last = parts[-1]
    if last in {"S", "M", "L", "paper"}:
        return last
    return None


def _pretty_framework_name(framework: str) -> str:
    """Convert a framework id like 'pytorch_gpu' to 'PyTorch GPU'."""
    if not framework:
        return framework
    parts = framework.split("_")
    head_map = {
        "pytorch": "PyTorch",
        "jax": "JAX",
        "numpy": "NumPy",
        "numba": "Numba",
        "cupy": "CuPy",
        "pythran": "Pythran",
        "legate": "Legate",
        "dpnp": "DPNP",
        "dace": "DaCe",
        "appy": "Appy",
    }
    pretty: List[str] = []
    if parts:
        pretty.append(head_map.get(parts[0], parts[0].title()))
        for p in parts[1:]:
            if p.lower() == "cpu":
                pretty.append("CPU")
            elif p.lower() == "gpu":
                pretty.append("GPU")
            else:
                pretty.append(p.replace("-", " ").title())
    return " ".join(pretty) if pretty else framework


def _extract_preset_from_series_label(series_label: str) -> Optional[str]:
    m = re.search(r"\((S|M|L|paper)\)\s*$", series_label)
    return m.group(1) if m else None


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
    # Exclude runs that use the library implementation (forward or backward).
    # Apply at load time so it affects all frameworks (including reference ones like jax_gpu).
    if "details" in data.columns:
        details = data["details"].astype("string")
        data = data[~details.str.contains("lib-implementation", na=False)]
    data = data[data["domain"] != ""]
    data = data[data["framework"].isin(frameworks)].reset_index(drop=True)
    return data


def _load_medians_for_unroll_dbs(
    dbs: List[Path],
    preset: str,
    framework: str,
    extra_frameworks: Optional[List[str]] = None,
) -> Dict[str, pd.DataFrame]:
    per_db_medians: Dict[str, pd.DataFrame] = {}
    frameworks = [framework] + list(extra_frameworks or [])
    for db in dbs:
        label = _unroll_label(db)
        try:
            raw = fetch_results_from_db(db, preset, frameworks)
        except Exception as exc:
            warnings.warn(f"Skipping DB {db}: {exc}", RuntimeWarning, stacklevel=2)
            continue
        if raw.empty:
            warnings.warn(
                f"No rows for frameworks={frameworks!r}, preset={preset!r} in {db}",
                RuntimeWarning,
                stacklevel=2,
            )
            continue

        # Require the primary framework to be present for this DB to be useful.
        if raw[raw["framework"] == framework].empty:
            warnings.warn(
                f"No rows for framework={framework!r}, preset={preset!r} in {db}",
                RuntimeWarning,
                stacklevel=2,
            )
            continue

        # Primary framework: keep existing behavior (choose best details variant).
        primary_raw = raw[raw["framework"] == framework].reset_index(drop=True)
        medians_primary, _filtered = pbr.select_best_runs(primary_raw)

        # Extra frameworks: compute a straight median across all details.
        medians_extra_frames: List[pd.DataFrame] = []
        for extra in list(extra_frameworks or []):
            extra_raw = raw[raw["framework"] == extra]
            if extra_raw.empty:
                continue
            med = (
                extra_raw.groupby(["benchmark", "framework", "mode"], dropna=False)
                .agg(time=("time", "median"))
                .reset_index()
            )
            med["time_ms"] = med["time"] * 1000.0
            medians_extra_frames.append(med)

        if medians_extra_frames:
            medians = pd.concat([medians_primary] + medians_extra_frames, ignore_index=True)
        else:
            medians = medians_primary

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
            f"{_pretty_framework_name(framework)} {mode} median runtime vs unroll (preset={preset})"
            if not relative_to_first
            else (
                f"{_pretty_framework_name(framework)} {mode} speedup vs unroll (preset={preset})"
                if speedup
                else f"{_pretty_framework_name(framework)} {mode} runtime scale vs unroll (preset={preset})"
            )
        )
    )
    ax.set_xlabel("Unroll factor")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (× vs first unroll)" if speedup else "Runtime scale (× first unroll)")
    )

    # Style: make x tick labels 2× larger; match y-axis label fontsize.
    base_tick = _font_size_points(plt.rcParams.get("xtick.labelsize", 10), default=10.0)
    big = base_tick * 2.0
    ax.tick_params(axis="x", labelsize=big)
    ax.yaxis.label.set_size(big)

    ax.set_xscale("log", base=2)
    ax.set_xticks(unroll_x)
    ax.set_xticklabels([str(int(x)) if float(x).is_integer() else str(x) for x in unroll_x])
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=2, subs="auto"))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())

    # Ensure the axis starts at 2^0 (unroll=1), even if the first data point is larger.
    try:
        ax.set_xlim(left=1)
    except Exception:
        pass

    if use_logscale:
        # For speedup plots, use base-2 log scaling to match 2^k tick labels.
        if relative_to_first and speedup:
            ax.set_yscale("log", base=2)
        else:
            ax.set_yscale("log")

    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    if use_logscale:
        # Minor ticks depend on the y-scale base.
        base = 2 if (relative_to_first and speedup) else 10
        ax.yaxis.set_minor_locator(ticker.LogLocator(base=base, subs="auto"))
        ax.yaxis.set_minor_formatter(ticker.NullFormatter())
    else:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.grid(axis="y", which="major", linestyle="--", alpha=0.4)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.25)
    ax.legend(title="benchmark", ncol=2)

    # Font sizing: unify all text and reduce by 30% vs last iteration.
    base_tick = _font_size_points(plt.rcParams.get("xtick.labelsize", 10), default=10.0)
    uniform = base_tick * 1.4  # previously 2.0×; now 30% smaller
    _apply_uniform_font(ax, uniform)

    # Speedup tick labels: label powers of 2 explicitly on log scale.
    if use_logscale and relative_to_first and speedup:
        all_y = []
        for line in ax.get_lines():
            ydata = line.get_ydata()
            if ydata is not None:
                all_y.append(np.asarray(ydata, dtype=float))
        if all_y:
            _set_speedup_power2_yticks(ax, np.concatenate(all_y))

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
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
    show_noncompiled: bool = True,
    only_benchmarks: Optional[List[str]] = None,
    bench: Optional[str] = None,
    series_to_kind: Optional[Dict[str, str]] = None,
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

    # Line style mapping:
    # - color encodes dataset/preset (S/M/L/paper)
    # - linestyle encodes compiled vs uncompiled
    compiled_style = "-"
    uncompiled_style = "--"
    # Reference styles (avoid clashing with compiled/uncompiled linestyles).
    jax_ref_style = ":"
    noncompiled_ref_style = "-."

    preset_colors = {
        "M": "tab:blue",
        "S": "tab:orange",
        "L": "tab:green",
        "paper": "tab:purple",
    }

    for series_label in sorted(series_to_per_db_medians.keys()):
        per_db = series_to_per_db_medians[series_label]
        preset = _extract_preset_from_series_label(series_label)
        series_color = preset_colors.get(preset or "")
        unroll_labels = sorted(per_db.keys(), key=_sort_key)

        kind = None
        if series_to_kind is not None:
            kind = series_to_kind.get(series_label)
        if kind is None:
            lowered = series_label.lower()
            is_uncompiled = (
                "uncompiled" in lowered or "no-compile" in lowered or "nocompile" in lowered
            )
            is_compiled = ("compiled" in lowered or "compile" in lowered) and not is_uncompiled
            if is_uncompiled:
                kind = "uncompiled"
            elif is_compiled:
                kind = "compiled"
        primary_linestyle = uncompiled_style if kind == "uncompiled" else compiled_style

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

        # Grab baseline (unroll=1) runtime for the primary framework if present.
        baseline_time_ms: Optional[float] = None
        if "1" in per_db:
            base_med = per_db["1"]
            base_subset = base_med[(base_med["framework"] == framework) & (base_med["mode"] == mode)]
            base_val = base_subset[base_subset["benchmark"] == bench]["time_ms"]
            if not base_val.empty:
                baseline_time_ms = float(base_val.iloc[0])

        if relative_to_first and ys:
            # Normalize to unroll=1 when available; otherwise fall back to the first x point.
            baseline = baseline_time_ms if baseline_time_ms is not None else ys[0]
            if baseline and not np.isnan(baseline) and baseline > 0:
                arr = np.asarray(ys, dtype=float)
                if speedup:
                    ys = (float(baseline) / arr).tolist()
                else:
                    ys = (arr / float(baseline)).tolist()
            else:
                warnings.warn(
                    f"Cannot normalize series {series_label!r}: missing/invalid baseline at unroll=1.",
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

        primary_line = ax.plot(
            xs,
            ys,
            marker="o",
            linewidth=1.8,
            markersize=4,
            color=series_color,
            linestyle=primary_linestyle,
            label="_nolegend_",
        )[0]

        # If the baseline DB also contains a jax_gpu run, plot it as a horizontal reference
        # line (same color as this series), expressed in the same units as the primary line.
        if "1" in per_db and baseline_time_ms is not None and baseline_time_ms > 0:
            base_med = per_db["1"]
            jax_subset = base_med[(base_med["framework"] == "jax_gpu") & (base_med["mode"] == mode)]
            jax_val = jax_subset[jax_subset["benchmark"] == bench]["time_ms"]
            if not jax_val.empty:
                jax_time_ms = float(jax_val.iloc[0])
                if relative_to_first:
                    jax_y = (baseline_time_ms / jax_time_ms) if speedup else (jax_time_ms / baseline_time_ms)
                else:
                    jax_y = jax_time_ms

                ax.plot(
                    xs,
                    [jax_y] * len(xs),
                    linestyle=jax_ref_style,
                    linewidth=1.8,
                    color=primary_line.get_color(),
                    label="_nolegend_",
                )

            # Also plot noncompiled (same framework) as a horizontal reference line.
            # Value is relative to the compiled unroll=1 baseline when normalizing.
            if show_noncompiled and "noncompiled" in per_db:
                nc_med = per_db["noncompiled"]
                nc_subset = nc_med[(nc_med["framework"] == framework) & (nc_med["mode"] == mode)]
                nc_val = nc_subset[nc_subset["benchmark"] == bench]["time_ms"]
                if not nc_val.empty:
                    nc_time_ms = float(nc_val.iloc[0])
                    if relative_to_first:
                        nc_y = (baseline_time_ms / nc_time_ms) if speedup else (nc_time_ms / baseline_time_ms)
                    else:
                        nc_y = nc_time_ms
                    ax.plot(
                        xs,
                        [nc_y] * len(xs),
                        linestyle=noncompiled_ref_style,
                        linewidth=1.8,
                        color=primary_line.get_color(),
                        label="_nolegend_",
                    )

    ax.set_title(
        (
            f"{_pretty_framework_name(framework)} {mode} median runtime vs unroll ({labels.get(bench, bench)})"
            if not relative_to_first
            else (
                f"{_pretty_framework_name(framework)} {mode} speedup vs unroll ({labels.get(bench, bench)})"
                if speedup
                else f"{_pretty_framework_name(framework)} {mode} runtime scale vs unroll ({labels.get(bench, bench)})"
            )
        )
    )
    ax.set_xlabel("Unroll factor")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (× vs first unroll)" if speedup else "Runtime scale (× first unroll)")
    )

    # Style: make x tick labels 2× larger; match y-axis label fontsize.
    base_tick = _font_size_points(plt.rcParams.get("xtick.labelsize", 10), default=10.0)
    big = base_tick * 2.0
    ax.tick_params(axis="x", labelsize=big)
    ax.yaxis.label.set_size(big)
    ax.set_xscale("log", base=2)
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=2, subs="auto"))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())

    # Ensure the axis starts at 2^0 (unroll=1), and add a small right padding so
    # the rightmost markers/lines don't get clipped.
    try:
        max_x = 1.0
        for line in ax.get_lines():
            xdata = np.asarray(line.get_xdata(), dtype=float)
            xdata = xdata[np.isfinite(xdata)]
            if xdata.size:
                max_x = max(max_x, float(np.max(xdata)))
        ax.set_xlim(left=1, right=max_x * 1.05)
    except Exception:
        pass

    if use_logscale:
        # For speedup plots, use base-2 log scaling to match 2^k tick labels.
        if relative_to_first and speedup:
            ax.set_yscale("log", base=2)
        else:
            ax.set_yscale("log")
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    if use_logscale:
        base = 2 if (relative_to_first and speedup) else 10
        ax.yaxis.set_minor_locator(ticker.LogLocator(base=base, subs="auto"))
        ax.yaxis.set_minor_formatter(ticker.NullFormatter())
    else:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.grid(axis="y", which="major", linestyle="--", alpha=0.4)
    ax.grid(axis="y", which="minor", linestyle=":", alpha=0.25)

    # Simplified legend:
    # - linestyle encodes compiled vs uncompiled
    # - color encodes dataset/preset
    kinds_present: set[str] = set()
    if series_to_kind is not None:
        kinds_present |= {k for k in series_to_kind.values() if k}
    else:
        for lbl in series_to_per_db_medians.keys():
            low = lbl.lower()
            is_uncompiled = ("uncompiled" in low or "no-compile" in low or "nocompile" in low)
            is_compiled = ("compiled" in low or "compile" in low) and not is_uncompiled
            if is_uncompiled:
                kinds_present.add("uncompiled")
            if is_compiled:
                kinds_present.add("compiled")

    style_handles: List[Line2D] = []
    if ("compiled" in kinds_present) or (not kinds_present):
        style_handles.append(
            Line2D(
                [0],
                [0],
                color="black",
                lw=2,
                linestyle=compiled_style,
                label=f"Compiled {_pretty_framework_name(framework)}",
            )
        )
    if "uncompiled" in kinds_present:
        style_handles.append(
            Line2D(
                [0],
                [0],
                color="black",
                lw=2,
                linestyle=uncompiled_style,
                label=f"Uncompiled {_pretty_framework_name(framework)}",
            )
        )
    if (not style_handles) and ("uncompiled" in kinds_present):
        # Only uncompiled series were provided.
        style_handles.append(
            Line2D(
                [0],
                [0],
                color="black",
                lw=2,
                linestyle=uncompiled_style,
                label=f"Uncompiled {_pretty_framework_name(framework)}",
            )
        )
    style_handles.append(
        Line2D(
            [0],
            [0],
            color="black",
            lw=2,
            linestyle=jax_ref_style,
            label=_pretty_framework_name("jax_gpu") + " (ref)",
        )
    )
    has_noncompiled = show_noncompiled and any(
        "noncompiled" in per_db for per_db in series_to_per_db_medians.values()
    )
    if has_noncompiled:
        style_handles.append(
            Line2D(
                [0],
                [0],
                color="black",
                lw=2,
                linestyle=noncompiled_ref_style,
                label=f"Noncompiled {_pretty_framework_name(framework)}",
            )
        )

    preset_colors = {
        "M": "tab:blue",
        "S": "tab:orange",
        "L": "tab:green",
        "paper": "tab:purple",
    }
    present_presets = [
        p
        for p in ["M", "S", "L", "paper"]
        if any(_extract_preset_from_series_label(k) == p for k in series_to_per_db_medians.keys())
    ]
    color_handles = [
        Line2D([0], [0], color=preset_colors[p], lw=2, linestyle="-", label=f"{p} dataset")
        for p in present_presets
    ]

    # Put legend outside so it doesn't hide the x=1 baseline points.
    ax.legend(
        handles=style_handles + color_handles,
        title="Series",
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0.0,
    )

    # Font sizing: unify all text and reduce by 30% vs last iteration.
    base_tick = _font_size_points(plt.rcParams.get("xtick.labelsize", 10), default=10.0)
    uniform = base_tick * 1.4  # previously 2.0×; now 30% smaller
    _apply_uniform_font(ax, uniform)

    # Speedup tick labels: label powers of 2 explicitly on log scale.
    if use_logscale and relative_to_first and speedup:
        all_y = []
        for line in ax.get_lines():
            ydata = line.get_ydata()
            if ydata is not None:
                all_y.append(np.asarray(ydata, dtype=float))
        if all_y:
            _set_speedup_power2_yticks(ax, np.concatenate(all_y))
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
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
        "--compiled-db-dirs",
        nargs="+",
        default=None,
        help=(
            "Directories containing compiled unroll DBs (npbench-unroll-*.db). "
            "When used with --uncompiled-db-dirs, plots both on the same chart."
        ),
    )
    parser.add_argument(
        "--uncompiled-db-dirs",
        nargs="+",
        default=None,
        help=(
            "Directories containing uncompiled unroll DBs (npbench-unroll-*.db). "
            "When used with --compiled-db-dirs, plots both on the same chart."
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
        default=True,
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
        "--show-noncompiled",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="Show noncompiled horizontal reference line (default: true).",
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

    compare_compiled = (args.compiled_db_dirs is not None) or (args.uncompiled_db_dirs is not None)
    multi_series = (args.db_dirs is not None) or compare_compiled

    output_dir = Path(args.output_dir) / args.results_subdir
    output_dir.mkdir(parents=True, exist_ok=True)

    bench_dir = Path(args.bench_info_dir)
    labels = pbr.load_benchmark_labels(bench_dir)
    resolved_benchmarks = _resolve_benchmark_args(args.benchmarks, bench_dir)

    if multi_series:
        # Build the series list.
        series_items: List[Tuple[Path, Optional[str], str]] = []
        # Tuple: (dir, preset_override, kind)
        if compare_compiled:
            for d in list(args.compiled_db_dirs or []):
                series_items.append((Path(d), None, "compiled"))
            for d in list(args.uncompiled_db_dirs or []):
                series_items.append((Path(d), None, "uncompiled"))
            # Allow mixing legacy --db-dirs with the compare mode (treated as unknown).
            for d in list(args.db_dirs or []):
                series_items.append((Path(d), None, "unknown"))
        else:
            for d in list(args.db_dirs or []):
                series_items.append((Path(d), None, "unknown"))

        db_dirs = [d for d, _preset, _kind in series_items]
        for d in db_dirs:
            if not d.is_dir():
                raise SystemExit(f"Not a directory: {d}")
        series_presets: List[Optional[str]]
        if args.series_presets is not None:
            if len(args.series_presets) != len(db_dirs):
                raise SystemExit(
                    "--series-presets must match the total number of series directories "
                    "(from --db-dirs and/or --compiled-db-dirs/--uncompiled-db-dirs)"
                )
            series_presets = list(args.series_presets)
        else:
            series_presets = [None] * len(db_dirs)

        series_to_per_db_medians: Dict[str, Dict[str, pd.DataFrame]] = {}
        series_to_kind: Dict[str, str] = {}
        for (d, _unused_preset, kind), preset_override in zip(series_items, series_presets):
            inferred = _infer_preset_from_name(d.name)
            preset = preset_override or inferred or args.preset
            dbs: List[Path] = []
            baseline_db = d / "npbench-baseline.db"
            if baseline_db.is_file():
                dbs.append(baseline_db)
            if args.show_noncompiled:
                noncompiled_db = d / "npbench-noncompiled.db"
                if noncompiled_db.is_file():
                    dbs.append(noncompiled_db)
            dbs.extend(sorted(d.glob("npbench-unroll-*.db")))
            if not dbs:
                warnings.warn(
                    f"No DBs found in {d} matching npbench-unroll-*.db",
                    RuntimeWarning,
                    stacklevel=1,
                )
                continue
            per_db_medians = _load_medians_for_unroll_dbs(
                dbs,
                preset,
                args.framework,
                extra_frameworks=["jax_gpu"],
            )
            if per_db_medians:
                label_prefix = d.name
                if kind in {"compiled", "uncompiled"}:
                    label_prefix = f"{d.name} {kind}"
                series_label = f"{label_prefix} ({preset})"
                series_to_per_db_medians[series_label] = per_db_medians
                if kind in {"compiled", "uncompiled"}:
                    series_to_kind[series_label] = kind

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
            show_noncompiled=args.show_noncompiled,
            only_benchmarks=resolved_benchmarks,
            series_to_kind=(series_to_kind if series_to_kind else None),
        )
    else:
        dbs = _discover_dbs(args.db_glob)
        baseline_db = Path("npbench-baseline.db")
        if baseline_db.is_file():
            dbs = [baseline_db] + dbs
        if not dbs:
            raise SystemExit(f"No DBs matched --db-glob={args.db_glob!r}")
        per_db_medians = _load_medians_for_unroll_dbs(
            dbs,
            args.preset,
            args.framework,
            extra_frameworks=["jax_gpu"],
        )
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
