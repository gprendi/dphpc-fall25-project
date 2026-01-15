import argparse
import json
import math
import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd

from npbench.infrastructure import utilities as util

EXEC_MODES = ("forward", "backward")
FRAMEWORK_DISPLAY = {
    "jax_cpu": "JAX CPU",
    "jax_gpu": "JAX GPU",
    "pytorch_cpu": "PyTorch CPU",
    "pytorch_gpu": "PyTorch GPU",
}
ABBREV_SPEEDUP_HEATMAP = "sh"
ABBREV_RUNTIME_BARS = "rb"
ABBREV_SPEEDUP_BARS = "sb"
ABBREV_BOX = "bx"

# Use a serif face for publication-ready plots and larger text.
rcParams["font.family"] = "Nimbus Roman"
rcParams["font.size"] = 16
rcParams["axes.titlesize"] = 22
rcParams["axes.labelsize"] = 18
rcParams["xtick.labelsize"] = 18
rcParams["ytick.labelsize"] = 20


def _filename(prefix: str, mode: str, preset: str, benches: List[str],
              scale: str = "", ext: str = "png") -> str:
    """
    Build filename like: prefix_mode_preset_k1_k2[...], with optional scale suffix.
    """
    kernels = "_".join(benches) if benches else "all"
    parts = [prefix, mode, preset, kernels]
    if scale:
        parts.append(scale)
    return "_".join(parts) + f".{ext}"


def my_round(value: float, width: int) -> str:
    fmt = f"{{:.{width}f}}"
    return fmt.format(value)


def my_speedup_abbr(value: float) -> str:
    prefix = ""
    label = ""
    if math.isnan(value):
        return ""
    if value < 1:
        prefix = "\u2193"
        value = 1 / value
    elif value > 1:
        prefix = "\u2191"
    if value > 100:
        value = int(value)
    if value > 1000:
        label = prefix + my_round(value / 1000, 1) + "k"
    else:
        label = prefix + my_round(value, 1)
    return label


def my_runtime_abbr(value: float) -> str:
    if math.isnan(value):
        return ""
    # Input is in seconds; show milliseconds as whole numbers.
    ms = int(round(value * 1000))
    return f"{ms}ms"


def my_mad_superscript(mad_pct: float) -> str:
    if mad_pct is None or math.isnan(mad_pct):
        return ""
    # Use mathtext superscript to keep the variance small and unobtrusive.
    return f"$^{{({my_round(mad_pct, 0)})}}$"


def load_benchmark_labels(bench_dir: Path) -> Dict[str, str]:
    labels: Dict[str, str] = {}
    for path in sorted(bench_dir.glob("*.json")):
        with path.open() as handle:
            payload = json.load(handle)
        bench = payload.get("benchmark", {})
        short_name = bench.get("short_name", path.stem)
        # Prefer concise kernel handles (e.g., k2mm) over descriptive long names.
        labels[short_name] = path.stem
    return labels


def fetch_results(presets: List[str], frameworks: List[str]) -> pd.DataFrame:
    conn = util.create_connection("dbs/linear_algebra_full2.db")
    placeholders = ",".join("?" for _ in presets)
    try:
        data = pd.read_sql_query(
            f"""
            SELECT benchmark, domain, framework, mode, details, time, preset
            FROM results
            WHERE preset IN ({placeholders})
              AND mode IN ('forward', 'backward')
            """,
            conn,
            params=tuple(presets),
        )
    except (pd.errors.DatabaseError, sqlite3.OperationalError) as exc:
        raise SystemExit(
            "Could not read benchmark results: missing 'results' table in npbench.db. "
            "Run benchmarks or point to the correct database before plotting."
        ) from exc
    data = data[data["domain"] != ""]
    data = data[data["framework"].isin(frameworks)].reset_index(drop=True)
    # Drop auxiliary JAX lib implementations; keep only primary runs
    data = data[~data["details"].str.contains("lib-implementation", na=False)]
    return data


def select_best_runs(results: pd.DataFrame
                     ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    grouped = (results.groupby(
        ["benchmark", "framework", "mode", "details"], dropna=False).agg(
            time=("time", "median")).reset_index())
    best = (
        grouped.sort_values("time")
        .groupby(["benchmark", "framework", "mode"], dropna=False)
        .first()
        .reset_index()
    )
    filtered = pd.merge(
        results,
        best.drop(columns=["time"]),
        on=["benchmark", "framework", "mode", "details"],
        how="inner",
    )
    filtered["time_ms"] = filtered["time"] * 1000.0
    medians = (
        filtered.groupby(["benchmark", "framework", "mode"],
                         dropna=False).agg(
                             time=("time", "median"),
                             mad=("time",
                                  lambda s: np.median(np.abs(
                                      s - np.median(s))))
                         ).reset_index())
    medians["time_ms"] = medians["time"] * 1000.0
    medians["mad_ms"] = medians["mad"] * 1000.0
    medians["mad_pct"] = np.where(
        medians["time"] > 0, medians["mad"] / medians["time"] * 100, np.nan
    )
    return medians, filtered


def _ordered_benchmarks(medians: pd.DataFrame,
                        labels: Dict[str, str],
                        bench_order: List[str] = None) -> List[str]:
    benches = sorted(medians["benchmark"].unique())
    if bench_order:
        available = set(benches)
        ordered: List[str] = []
        seen = set()
        for b in bench_order:
            if b in available and b not in seen:
                ordered.append(b)
                seen.add(b)
        remaining = [b for b in benches if b not in seen]
        remaining.sort(key=lambda b: labels.get(b, b))
        return ordered + remaining
    benches.sort(key=lambda b: labels.get(b, b))
    return benches


def _pivot_times(medians: pd.DataFrame) -> pd.DataFrame:
    return medians.pivot_table(index="benchmark",
                               columns=["framework", "mode"],
                               values="time_ms")


def plot_speedup_heatmap(medians: pd.DataFrame, labels: Dict[str, str],
                         frameworks: List[str], baseline: str, preset: str,
                         output_dir: Path, hide_bench_labels: bool = False,
                         bench_order: List[str] = None,
                         output_format: str = "png"):

    pivot = _pivot_times(medians)
    benches = _ordered_benchmarks(medians, labels, bench_order)
    bench_labels = [labels.get(b, b) for b in benches]
    mad_lookup = medians.set_index(["benchmark", "framework", "mode"])["mad_pct"]

    # Compute ratio tables
    ratio_tables = {}
    baseline_times = {}
    for mode in EXEC_MODES:
        base = pivot[(baseline, mode)]
        ratios = {}
        for framework in frameworks:
            ratios[framework] = base / pivot[(framework, mode)]
        ratio_tables[mode] = pd.DataFrame(ratios).reindex(benches)
        baseline_times[mode] = base.reindex(benches)

    norm = LogNorm(vmin=0.5, vmax=2.0)

    def _render_heatmap(ax, mode: str, df: pd.DataFrame, base_times: pd.Series,
                        *, show_ylabel: bool):
        im = ax.imshow(
            df.to_numpy(),
            cmap="RdYlGn",
            norm=norm,   # log scale
            aspect="auto"
        )

        # ticks
        if hide_bench_labels:
            ax.set_yticks([])
            ax.set_yticklabels([])
        else:
            ax.set_yticks(np.arange(len(benches)))
            if show_ylabel:
                ax.set_yticklabels(bench_labels, rotation=40, ha="right", va="center")
            else:
                ax.set_yticklabels([])
        ax.set_xticks(np.arange(len(frameworks)))
        ax.set_xticklabels(
            [FRAMEWORK_DISPLAY.get(fw, fw.replace("_", " ").title()) for fw in frameworks],
            rotation=40, ha="right"
        )
        ax.set_title(f"{mode.title()} Speedup")

        # Add ratio text (abbreviated)
        for i, bench in enumerate(benches):
            for j, framework in enumerate(frameworks):
                value = df.iloc[i, j]
                label = my_speedup_abbr(value)
                mad_pct = mad_lookup.get((bench, framework, mode), np.nan)
                suffix = my_mad_superscript(mad_pct)
                if framework == baseline:
                    runtime_ms = base_times.iloc[i]
                    label = ""
                    if not math.isnan(runtime_ms):
                        label = my_runtime_abbr(runtime_ms / 1000.0)
                    label += suffix
                else:
                    label += suffix
                ax.text(
                    j, i, label,
                    ha="center", va="center", color="black"
                )
        return im

    # ----- helper to plot one mode -----
    def _plot_single(mode: str, df: pd.DataFrame, base_times: pd.Series):
        fig_width = max(5, len(frameworks) * 1.05)
        fig_height = max(4, len(benches) * 0.5)

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        im = _render_heatmap(ax, mode, df, base_times, show_ylabel=True)

        fig.tight_layout()
        filename = _filename(ABBREV_SPEEDUP_HEATMAP, mode, preset, benches,
                             ext=output_format)
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    def _plot_combined():
        # Wider cells (more horizontal) and tighter spacing between the two heatmaps.
        fig_width = max(9.0, len(frameworks) * 2.6)
        fig_height = max(3.6, len(benches) * 0.9)
        fig, axes = plt.subplots(
            1,
            2,
            figsize=(fig_width, fig_height),
            sharey=True,
            gridspec_kw={"wspace": 0.01},
        )
        fig.subplots_adjust(left=0.1, right=0.88, top=0.9, bottom=0.23, wspace=0.01)

        _render_heatmap(axes[0], "forward", ratio_tables["forward"],
                        baseline_times["forward"], show_ylabel=True)
        im = _render_heatmap(axes[1], "backward", ratio_tables["backward"],
                             baseline_times["backward"],
                             show_ylabel=not hide_bench_labels)

        # Place colorbar to the far right to avoid squeezing the plots.
        cax = fig.add_axes([0.89, 0.23, 0.015, 0.67])
        cbar = fig.colorbar(im, cax=cax)
        filename = _filename(ABBREV_SPEEDUP_HEATMAP, "both", preset, benches,
                             ext=output_format)
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    # ----- generate 3 PNGs -----
    # _plot_single("forward", ratio_tables["forward"], baseline_times["forward"])
    # _plot_single("backward", ratio_tables["backward"], baseline_times["backward"])
    _plot_combined()





def main():
    parser = argparse.ArgumentParser(
        description="Visualise GPU backprop benchmark results.")
    parser.add_argument("-p",
                        "--preset",
                        nargs="+",
                        default=["S"],
                        help=("Preset/size selection. "
                              "Provide one value to use for all kernels, or a list "
                              "matching --benchmarks length to specify per-kernel sizes "
                              "(e.g. -k k2mm k3mm atax gemver -p M M L M)."))
    parser.add_argument("-o",
                        "--output-dir",
                        default="ad_plots",
                        help="Directory for generated figures.")
    parser.add_argument("--format",
                        default="eps",
                        choices=["png", "eps", "pdf", "svg"],
                        help="Output figure format/extension.")
    parser.add_argument("-f",
                        "--frameworks",
                        nargs="+",
                        default=["jax_cpu","jax_gpu", "pytorch_cpu", "pytorch_gpu"],
                        help="Frameworks to include in the plots.")
    parser.add_argument("-k",
                        "--benchmarks",
                        nargs="+",
                        default=None,
                        help="Optional list of benchmark kernels to include (e.g. k2mm k3mm atax gemver).")
    parser.add_argument("-b",
                        "--baseline",
                        default="jax_cpu",
                        help="Framework to use as baseline for ratio plots.")
    parser.add_argument("--hide-bench-labels",
                        action="store_true",
                        help="Remove kernel labels and ticks on the heatmap y-axis.")
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_format = args.format
    labels = load_benchmark_labels(Path("bench_info"))
    frameworks = args.frameworks
    if args.baseline not in frameworks:
        raise SystemExit("Baseline framework must be part of --frameworks.")

    preset_args = args.preset
    if len(preset_args) > 1 and not args.benchmarks:
        raise SystemExit("Provide --benchmarks when supplying multiple presets.")
    if len(preset_args) > 1 and len(preset_args) != len(args.benchmarks):
        raise SystemExit("--preset count must match --benchmarks count when providing multiple presets.")

    raw_results = fetch_results(preset_args, frameworks)
    bench_order: List[str] = None

    # Optional benchmark filtering with simple alias support (strip leading 'k')
    if args.benchmarks:
        available = set(raw_results["benchmark"].unique())
        bench_preset_pairs = []
        bench_order = []
        for idx, b in enumerate(args.benchmarks):
            target = b
            if target not in available and target.startswith("k"):
                alt = target[1:]
                if alt in available:
                    target = alt
            preset_val = preset_args[0] if len(preset_args) == 1 else preset_args[idx]
            bench_preset_pairs.append((b, target, preset_val))
            bench_order.append(target)

        mask = None
        missing = []
        for original, target, preset_val in bench_preset_pairs:
            if target not in available:
                missing.append(original)
                continue
            pair_mask = (
                (raw_results["benchmark"] == target) &
                (raw_results["preset"] == preset_val)
            )
            mask = pair_mask if mask is None else (mask | pair_mask)
        if mask is None:
            raw_results = raw_results.iloc[0:0]
        else:
            raw_results = raw_results[mask]
            if bench_order:
                present = set(raw_results["benchmark"].unique())
                bench_order = [b for b in bench_order if b in present]
        if missing:
            print(f"Warning: no data for requested benchmarks: {', '.join(missing)}")

    if raw_results.empty:
        raise SystemExit("No benchmark results found for the requested preset/benchmarks.")

    preset_label = preset_args[0] if len(preset_args) == 1 else "multi"

    medians, filtered = select_best_runs(raw_results)
    plot_speedup_heatmap(medians, labels, frameworks, args.baseline, preset_label,
                         output_dir, hide_bench_labels=args.hide_bench_labels,
                         bench_order=bench_order, output_format=output_format)


if __name__ == "__main__":
    main()
