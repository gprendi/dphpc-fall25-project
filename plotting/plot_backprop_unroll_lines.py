#!/usr/bin/env python3

import argparse
import json
import re
import warnings
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from cycler import cycler
from matplotlib import ticker
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

import plot_backprop_results as pbr
from npbench.infrastructure import utilities as util

PAPER_COLORS = [
    "#11427A",  # deep blue
    "#65AD66",  # green
    "#B84A00",  # brick
    "#7A5EA7",  # purple
    "#2C7C9E",  # teal
    "#C04B58",  # red
    "#8C8C8C",  # gray
    "#C59D0C",  # gold
]
PAPER_TEXT_COLOR = "#333333"
PAPER_REF_COLOR = "#444444"
PAPER_LABEL_SIZE = 20
PAPER_TICK_SIZE = 20
PAPER_TITLE_SIZE = 21
PAPER_LEGEND_SIZE = 17
PAPER_LEGEND_TITLE_SIZE = 12
PAPER_LINEWIDTH = 2.5
PAPER_MARKERSIZE = 6
PRESET_COLORS = {
    "M": PAPER_COLORS[0],
    "S": PAPER_COLORS[1],
    "L": PAPER_COLORS[2],
    "paper": PAPER_COLORS[3],
}

matplotlib.rcParams.update(
    {
        "font.family": "Nimbus Roman",
        "font.cursive": ["Nimbus Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Nimbus Roman",
        "mathtext.it": "Nimbus Roman:italic",
        "mathtext.bf": "Nimbus Roman:bold",
        "mathtext.cal": "Nimbus Roman:italic",
        "mathtext.tt": "DejaVu Sans Mono",
        "axes.prop_cycle": cycler(color=PAPER_COLORS),
    }
)


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


def _apply_paper_axes_style(ax: plt.Axes) -> None:
    ax.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_visible(True)
        ax.spines[side].set_color(PAPER_TEXT_COLOR)
    ax.tick_params(axis="both", which="both", labelsize=PAPER_TICK_SIZE, colors=PAPER_TEXT_COLOR)
    ax.xaxis.label.set_size(PAPER_LABEL_SIZE)
    ax.yaxis.label.set_size(PAPER_LABEL_SIZE)
    ax.xaxis.label.set_color(PAPER_TEXT_COLOR)
    ax.yaxis.label.set_color(PAPER_TEXT_COLOR)
    ax.title.set_size(PAPER_TITLE_SIZE)
    ax.title.set_color(PAPER_TEXT_COLOR)


def _lighten_color(color: object, amount: float = 0.5) -> Tuple[float, float, float]:
    try:
        rgb = mcolors.to_rgb(color)
    except ValueError:
        rgb = mcolors.to_rgb("gray")
    return tuple((1 - amount) * c + amount for c in rgb)


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
    """Convert a framework id like 'pytorch_gpu' to 'PyTorch'."""
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
            # elif p.lower() == "gpu":
            #     pretty.append("GPU")
            # else:
            #     pretty.append(p.replace("-", " ").title())
    return " ".join(pretty) if pretty else framework


def _extract_preset_from_series_label(series_label: str) -> Optional[str]:
    m = re.search(r"\((S|M|L|paper)\)\s*$", series_label)
    return m.group(1) if m else None


def _format_bench_label(
    bench: str,
    labels: Dict[str, str],
    display_labels: Optional[Dict[str, str]] = None,
) -> str:
    name = display_labels.get(bench) if display_labels else None
    if not name:
        name = labels.get(bench, bench)
    return (name or bench).replace(" ", "_")


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


def _load_benchmark_display_names(bench_dir: Path) -> Dict[str, str]:
    """Map DB short_names to display-friendly benchmark IDs (e.g. go_fast)."""
    display: Dict[str, str] = {}
    for path in sorted(bench_dir.glob("*.json")):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        bench = payload.get("benchmark", {}) if isinstance(payload, dict) else {}
        short_name = bench.get("short_name")
        if not short_name:
            continue
        display_name = bench.get("relative_path") or bench.get("module_name") or path.stem
        display[short_name] = display_name
    return display


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
        medians_primary, filtered = pbr.select_best_runs(primary_raw)
        minmax_primary = (
            filtered.groupby(["benchmark", "framework", "mode"], dropna=False)
            .agg(time_min=("time", "min"), time_max=("time", "max"))
            .reset_index()
        )
        minmax_primary["time_ms_min"] = minmax_primary["time_min"] * 1000.0
        minmax_primary["time_ms_max"] = minmax_primary["time_max"] * 1000.0
        medians_primary = medians_primary.merge(
            minmax_primary[["benchmark", "framework", "mode", "time_ms_min", "time_ms_max"]],
            on=["benchmark", "framework", "mode"],
            how="left",
        )

        # Extra frameworks: compute a straight median across all details.
        medians_extra_frames: List[pd.DataFrame] = []
        for extra in list(extra_frameworks or []):
            extra_raw = raw[raw["framework"] == extra]
            if extra_raw.empty:
                continue
            med = (
                extra_raw.groupby(["benchmark", "framework", "mode"], dropna=False)
                .agg(time=("time", "median"), time_min=("time", "min"), time_max=("time", "max"))
                .reset_index()
            )
            med["time_ms"] = med["time"] * 1000.0
            med["time_ms_min"] = med["time_min"] * 1000.0
            med["time_ms_max"] = med["time_max"] * 1000.0
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

    fig_width = max(8, len(unroll_x) * 0.2)
    fig, ax = plt.subplots(figsize=(fig_width, 6))

    # One line per benchmark (y = median runtime for this benchmark at each unroll).
    for bench in benches:
        ys: List[float] = []
        ymins: List[float] = []
        ymaxs: List[float] = []
        for label in keep_labels:
            med = per_db_medians[label]
            subset = med[(med["framework"] == framework) & (med["mode"] == mode)]
            val = subset[subset["benchmark"] == bench]["time_ms"]
            if val.empty:
                ys.append(np.nan)
                ymins.append(np.nan)
                ymaxs.append(np.nan)
                continue
            y_val = float(val.iloc[0])
            ys.append(y_val)
            if "time_ms_min" in subset.columns and "time_ms_max" in subset.columns:
                ymins.append(float(subset[subset["benchmark"] == bench]["time_ms_min"].iloc[0]))
                ymaxs.append(float(subset[subset["benchmark"] == bench]["time_ms_max"].iloc[0]))
            else:
                ymins.append(y_val)
                ymaxs.append(y_val)

        if relative_to_first:
            baseline = ys[0] if ys else np.nan
            if baseline and not np.isnan(baseline) and baseline > 0:
                arr = np.asarray(ys, dtype=float)
                arr_min = np.asarray(ymins, dtype=float)
                arr_max = np.asarray(ymaxs, dtype=float)
                if speedup:
                    ys = (float(baseline) / arr).tolist()
                    lower = float(baseline) / arr_max
                    upper = float(baseline) / arr_min
                else:
                    ys = (arr / float(baseline)).tolist()
                    lower = arr_min / float(baseline)
                    upper = arr_max / float(baseline)
                ymins = np.minimum(lower, upper).tolist()
                ymaxs = np.maximum(lower, upper).tolist()
            else:
                warnings.warn(
                    f"Cannot normalize benchmark {bench!r}: missing/invalid baseline at first unroll.",
                    RuntimeWarning,
                    stacklevel=2,
                )
        line = ax.plot(
            unroll_x,
            ys,
            marker="o",
            linewidth=PAPER_LINEWIDTH,
            markersize=PAPER_MARKERSIZE,
            alpha=0.9,
            label=labels.get(bench, bench),
            zorder=3,
        )[0]
        shade = _lighten_color(line.get_color(), amount=0.5)
        ax.fill_between(
            unroll_x,
            ymins,
            ymaxs,
            color=shade,
            linewidth=0,
            zorder=1,
        )

    ax.set_title(
        (
            f"{_pretty_framework_name(framework)} {mode} median runtime vs unroll (preset={preset})"
            if not relative_to_first
            else (
                f"{_pretty_framework_name(framework)} Backward Speedup vs Unroll Length (preset={preset})"
                if speedup
                else f"{_pretty_framework_name(framework)} {mode} runtime scale vs unroll (preset={preset})"
            )
        ),
        fontweight="normal",
    )
    ax.set_xlabel("Compiled Chunks", fontweight="normal")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (vs. Unroll Length = 1)" if speedup else "Runtime scale (× first unroll)"),
        fontweight="normal",
    )

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
    ax.legend(
        title="benchmark",
        ncol=2,
        loc="upper left",
        frameon=True,
        facecolor="white",
        framealpha=1.0,
        edgecolor="white",
        fontsize=PAPER_LEGEND_SIZE,
        title_fontsize=PAPER_LEGEND_TITLE_SIZE,
    )

    # Speedup tick labels: label powers of 2 explicitly on log scale.
    if use_logscale and relative_to_first and speedup:
        all_y = []
        for line in ax.get_lines():
            ydata = line.get_ydata()
            if ydata is not None:
                all_y.append(np.asarray(ydata, dtype=float))
        if all_y:
            _set_speedup_power2_yticks(ax, np.concatenate(all_y))
    _apply_paper_axes_style(ax)

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
    display_labels: Optional[Dict[str, str]] = None,
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

    for series_label in sorted(series_to_per_db_medians.keys()):
        per_db = series_to_per_db_medians[series_label]
        preset = _extract_preset_from_series_label(series_label)
        series_color = PRESET_COLORS.get(preset or "")
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
        ymins: List[float] = []
        ymaxs: List[float] = []
        for label in unroll_labels:
            x = _as_float(label)
            if x is None:
                continue
            med = per_db[label]
            subset = med[(med["framework"] == framework) & (med["mode"] == mode)]
            val = subset[subset["benchmark"] == bench]["time_ms"]
            xs.append(x)
            if val.empty:
                ys.append(np.nan)
                ymins.append(np.nan)
                ymaxs.append(np.nan)
                continue
            y_val = float(val.iloc[0])
            ys.append(y_val)
            if "time_ms_min" in subset.columns and "time_ms_max" in subset.columns:
                ymins.append(float(subset[subset["benchmark"] == bench]["time_ms_min"].iloc[0]))
                ymaxs.append(float(subset[subset["benchmark"] == bench]["time_ms_max"].iloc[0]))
            else:
                ymins.append(y_val)
                ymaxs.append(y_val)

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
                arr_min = np.asarray(ymins, dtype=float)
                arr_max = np.asarray(ymaxs, dtype=float)
                if speedup:
                    ys = (float(baseline) / arr).tolist()
                    lower = float(baseline) / arr_max
                    upper = float(baseline) / arr_min
                else:
                    ys = (arr / float(baseline)).tolist()
                    lower = arr_min / float(baseline)
                    upper = arr_max / float(baseline)
                ymins = np.minimum(lower, upper).tolist()
                ymaxs = np.maximum(lower, upper).tolist()
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
            linewidth=PAPER_LINEWIDTH,
            markersize=PAPER_MARKERSIZE,
            alpha=0.9,
            color=series_color,
            linestyle=primary_linestyle,
            label="_nolegend_",
            zorder=3,
        )[0]
        shade = _lighten_color(primary_line.get_color(), amount=0.5)
        ax.fill_between(
            xs,
            ymins,
            ymaxs,
            color=shade,
            linewidth=0,
            zorder=1,
        )

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
                    linewidth=PAPER_LINEWIDTH,
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
                        linewidth=PAPER_LINEWIDTH,
                        color=primary_line.get_color(),
                        label="_nolegend_",
                    )

    bench_label = _format_bench_label(bench, labels, display_labels)
    bench_label_tex = bench_label.replace("_", "\\_")
    if not relative_to_first:
        title = (
            f"{_pretty_framework_name(framework)} {mode} median runtime vs unroll "
            f"($\\mathtt{{{bench_label_tex}}}$)"
        )
    elif speedup:
        title = (
            f"{_pretty_framework_name(framework)} Backward Speedup vs. Unroll Length "
            f"($\\mathtt{{{bench_label_tex}}}$)"
        )
    else:
        title = (
            f"{_pretty_framework_name(framework)} {mode} runtime scale vs unroll "
            f"($\\mathtt{{{bench_label_tex}}}$)"
        )
    ax.set_title(title, fontweight="normal")
    ax.set_xlabel("Unroll Length", fontweight="normal")
    ax.set_ylabel(
        "Median runtime (ms)"
        if not relative_to_first
        else ("Speedup (vs. Unroll Length = 1)" if speedup else "Runtime scale (× first unroll)"),
        fontweight="normal",
    )

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

    # Legend:
    # - JAX + noncompiled refs in neutral color
    # - Unrolled PyTorch shown as solid line with a dot
    # - dataset colors shown with markers (no line)
    has_jax_ref = False
    has_noncompiled_ref = False
    for per_db in series_to_per_db_medians.values():
        if "1" in per_db:
            base_med = per_db["1"]
            jax_subset = base_med[(base_med["framework"] == "jax_gpu") & (base_med["mode"] == mode)]
            if not jax_subset.empty:
                has_jax_ref = True
        if show_noncompiled and "noncompiled" in per_db:
            nc_med = per_db["noncompiled"]
            nc_subset = nc_med[(nc_med["framework"] == framework) & (nc_med["mode"] == mode)]
            if not nc_subset.empty:
                has_noncompiled_ref = True

    style_handles: List[Line2D] = []
    if has_jax_ref:
        style_handles.append(
            Line2D(
                [0],
                [0],
                color=PAPER_REF_COLOR,
                lw=PAPER_LINEWIDTH,
                linestyle=jax_ref_style,
                label=f"{_pretty_framework_name("jax_gpu")} compiled",
            )
        )
    if has_noncompiled_ref:
        style_handles.append(
            Line2D(
                [0],
                [0],
                color=PAPER_REF_COLOR,
                lw=PAPER_LINEWIDTH,
                linestyle=noncompiled_ref_style,
                label=f"{_pretty_framework_name(framework)} noncompiled",
            )
        )
    style_handles.append(
        Line2D(
            [0],
            [0],
            color=PAPER_REF_COLOR,
            lw=PAPER_LINEWIDTH,
            linestyle=compiled_style,
            marker="o",
            markersize=PAPER_MARKERSIZE,
            label=f"{_pretty_framework_name(framework)} unrolled compiled",
        )
    )

    present_presets = [
        p
        for p in ["M", "S", "L", "paper"]
        if any(_extract_preset_from_series_label(k) == p for k in series_to_per_db_medians.keys())
    ]

    color_handles = [
        Patch(
            facecolor=PRESET_COLORS[p],
            edgecolor="none",
            label="Dataset 1 (larger)" if p == "M" else "Dataset 2 (smaller)",
        )
        for p in present_presets
    ]

    spacer = []
    if color_handles:
        spacer = [Patch(facecolor="none", edgecolor="none", label=" ")]

    # Put legend outside so it doesn't hide the x=1 baseline points.
    ax.legend(
        handles=style_handles + spacer + color_handles,
        loc="upper left",
        bbox_to_anchor=(0.0, 0.95),
        frameon=False,
        fontsize=PAPER_LEGEND_SIZE,
    )

    # Speedup tick labels: label powers of 2 explicitly on log scale.
    if use_logscale and relative_to_first and speedup:
        all_y = []
        for line in ax.get_lines():
            ydata = line.get_ydata()
            if ydata is not None:
                all_y.append(np.asarray(ydata, dtype=float))
        if all_y:
            _set_speedup_power2_yticks(ax, np.concatenate(all_y))
    _apply_paper_axes_style(ax)
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

    output_dir = Path(args.output_dir) #/ args.results_subdir
    output_dir.mkdir(parents=True, exist_ok=True)

    bench_dir = Path(args.bench_info_dir)
    labels = pbr.load_benchmark_labels(bench_dir)
    display_labels = _load_benchmark_display_names(bench_dir)
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
        out_name = f"backprop_unroll_lines_{args.framework}_{args.mode}_{bench_tag or 'one_bench'}_series.eps"
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
            display_labels=display_labels,
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

        out_name = f"backprop_unroll_lines_{args.framework}_{args.mode}_{args.preset}.eps"
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
