import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd

from npbench.infrastructure import utilities as util

EXEC_MODES = ("forward", "backward")

def _plot_stacked_bars(
    benches, frameworks, forward_times, backward_times,
    labels, output_path, use_logscale, ylabel_suffix
):
    """
    Shared helper for absolute and speedup bar plots.
    `forward_times` and `backward_times` must already contain the values to plot.
    """

    x = np.arange(len(benches))
    width = 0.8 / max(1, len(frameworks))
    cmap = plt.get_cmap("tab10")

    fig, ax = plt.subplots(figsize=(max(8, len(benches) * 0.6), 6))

    # For building a clean legend: one entry per framework only
    legend_handles = []
    legend_labels = []

    for f_idx, framework in enumerate(frameworks):
        centers = x + (f_idx - (len(frameworks) - 1) / 2) * width

        fw_vals = [forward_times.get((bench, framework), np.nan) for bench in benches]
        bw_vals = [backward_times.get((bench, framework), np.nan) for bench in benches]

        color = cmap(f_idx % cmap.N)

        # Full backward runtime = dark transparent
        h1 = ax.bar(
            centers,
            bw_vals,
            width=width,
            color=color,
            alpha=0.6,
        )
        # Forward portion = opaque
        ax.bar(
            centers,
            fw_vals,
            width=width,
            color=color,
            alpha=1.0,
        )

        # Only add one legend entry per framework
        legend_handles.append(h1)
        legend_labels.append(framework.replace("_", " ").title())

    ax.set_ylabel(f"Backward runtime {ylabel_suffix}\n(forward = solid lower part)")
    ax.set_xticks(x)
    ax.set_xticklabels([labels.get(b, b) for b in benches], rotation=30, ha="right")
    ax.legend(legend_handles, legend_labels, ncol=2)

    if use_logscale:
        ax.set_yscale("log")

    ax.grid(axis="y", linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


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
    suffix = " s"
    if math.isnan(value):
        return ""
    if value < 0.1:
        value *= 1000
        suffix = " ms"
    return f"{my_round(value, 2)}{suffix}"


def load_benchmark_labels(bench_dir: Path) -> Dict[str, str]:
    labels: Dict[str, str] = {}
    for path in sorted(bench_dir.glob("*.json")):
        with path.open() as handle:
            payload = json.load(handle)
        bench = payload.get("benchmark", {})
        short_name = bench.get("short_name", path.stem)
        labels[short_name] = bench.get("name", short_name)
    return labels


def fetch_results(preset: str, frameworks: List[str]) -> pd.DataFrame:
    conn = util.create_connection("npbench.db")
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
                         dropna=False).agg(time=("time", "median")).reset_index())
    medians["time_ms"] = medians["time"] * 1000.0
    return medians, filtered


def _ordered_benchmarks(medians: pd.DataFrame,
                        labels: Dict[str, str]) -> List[str]:
    benches = sorted(medians["benchmark"].unique())
    benches.sort(key=lambda b: labels.get(b, b))
    return benches


def _pivot_times(medians: pd.DataFrame) -> pd.DataFrame:
    return medians.pivot_table(index="benchmark",
                               columns=["framework", "mode"],
                               values="time_ms")


def plot_speedup_heatmap(medians: pd.DataFrame, labels: Dict[str, str],
                         frameworks: List[str], baseline: str, preset: str,
                         output_dir: Path):

    pivot = _pivot_times(medians)
    benches = _ordered_benchmarks(medians, labels)

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

    # ----- helper to plot one mode -----
    def _plot_single(mode: str, df: pd.DataFrame, base_times: pd.Series):
        fig_width = max(6, len(frameworks) * 1.4)
        fig_height = max(4, len(benches) * 0.5)

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))

        im = ax.imshow(
            df.to_numpy(),
            cmap="RdYlGn",
            norm=LogNorm(vmin=0.5, vmax=2.0),   # log scale
            aspect="auto"
        )

        # ticks
        ax.set_yticks(np.arange(len(benches)))
        ax.set_yticklabels([labels.get(b, b) for b in benches])
        ax.set_xticks(np.arange(len(frameworks)))
        ax.set_xticklabels(
            [fw.replace("_", " ").title() for fw in frameworks],
            rotation=30, ha="right"
        )

        ax.set_title(f"{mode.title()} speedup vs. {baseline}")

        # Add ratio text (abbreviated)
        for i, bench in enumerate(benches):
            for j, framework in enumerate(frameworks):
                value = df.iloc[i, j]
                label = my_speedup_abbr(value)
                if framework == baseline:
                    runtime_ms = base_times.iloc[i]
                    label = ""
                    if not math.isnan(runtime_ms):
                        label = my_runtime_abbr(runtime_ms / 1000.0)
                ax.text(
                    j, i, label,
                    ha="center", va="center", color="black"
                )

        fig.colorbar(im, ax=ax, shrink=0.8, label="Speedup (baseline / framework) [log scale]")
        fig.tight_layout()
        fig.savefig(output_dir / f"backprop_speedup_heatmap_{mode}_{preset}.png", dpi=300)
        plt.close(fig)

    # ----- generate 2 separate PNGs -----
    _plot_single("forward", ratio_tables["forward"], baseline_times["forward"])
    _plot_single("backward", ratio_tables["backward"], baseline_times["backward"])


def plot_runtime_bars(medians: pd.DataFrame, labels: Dict[str, str],
                      frameworks: List[str], preset: str, output_dir: Path):

    benches = _ordered_benchmarks(medians, labels)

    forward_times = medians[medians["mode"] == "forward"].set_index(
        ["benchmark", "framework"])["time_ms"]

    backward_times = medians[medians["mode"] == "backward"].set_index(
        ["benchmark", "framework"])["time_ms"]

    # Linear scale
    _plot_stacked_bars(
        benches, frameworks, forward_times, backward_times,
        labels, output_dir / f"backprop_runtime_bars_linear_{preset}.png",
        use_logscale=False,
        ylabel_suffix="(ms)"
    )

    # Log scale
    _plot_stacked_bars(
        benches, frameworks, forward_times, backward_times,
        labels, output_dir / f"backprop_runtime_bars_log_{preset}.png",
        use_logscale=True,
        ylabel_suffix="(ms, log scale)"
    )

def plot_speedup_bars(medians: pd.DataFrame, labels: Dict[str, str],
                      frameworks: List[str], baseline: str, preset: str,
                      output_dir: Path):

    benches = _ordered_benchmarks(medians, labels)

    fw = medians[medians["mode"] == "forward"].set_index(
        ["benchmark", "framework"])["time_ms"]
    bw = medians[medians["mode"] == "backward"].set_index(
        ["benchmark", "framework"])["time_ms"]

    # Compute speedup relative to baseline
    forward_speedup = {}
    backward_speedup = {}

    for bench in benches:
        f_base = fw.get((bench, baseline), np.nan)
        b_base = bw.get((bench, baseline), np.nan)
        for fwk in frameworks:
            f_val = fw.get((bench, fwk), np.nan)
            b_val = bw.get((bench, fwk), np.nan)
            forward_speedup[(bench, fwk)] = f_base / f_val if f_val > 0 else np.nan
            backward_speedup[(bench, fwk)] = b_base / b_val if b_val > 0 else np.nan

    forward_speedup_series = pd.Series(forward_speedup)
    backward_speedup_series = pd.Series(backward_speedup)

    # Linear scale
    _plot_stacked_bars(
        benches, frameworks,
        forward_speedup_series, backward_speedup_series,
        labels, output_dir / f"backprop_speedup_bars_linear_{preset}.png",
        use_logscale=False,
        ylabel_suffix=f"(speedup vs. {baseline})"
    )

    # Log scale
    _plot_stacked_bars(
        benches, frameworks,
        forward_speedup_series, backward_speedup_series,
        labels, output_dir / f"backprop_speedup_bars_log_{preset}.png",
        use_logscale=True,
        ylabel_suffix=f"(speedup vs. {baseline}, log scale)"
    )


def plot_runtime_boxplots(filtered: pd.DataFrame, frameworks: List[str],
                          preset: str, output_dir: Path):
    cmap = plt.get_cmap("tab10")
    fig, axes = plt.subplots(1,
                             len(EXEC_MODES),
                             figsize=(max(6, len(frameworks) * 1.2), 4),
                             sharey=True)
    for idx, mode in enumerate(EXEC_MODES):
        ax = axes[idx]
        ax.set_title(f"{mode.title()} runtimes")
        data = []
        labels = []
        colors = []
        for f_idx, framework in enumerate(frameworks):
            subset = filtered[(filtered["framework"] == framework)
                              & (filtered["mode"] == mode)]
            if subset.empty:
                continue
            data.append(subset["time_ms"].to_numpy())
            labels.append(framework.replace("_", " ").title())
            colors.append(cmap(f_idx % cmap.N))
        if not data:
            continue
        bp = ax.boxplot(data,
                        tick_labels=labels,
                        showfliers=False,
                        patch_artist=True)
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        ax.set_yscale("log")
        ax.set_ylabel("Runtime (ms)")
        ax.grid(axis="y", linestyle="--", alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_dir / f"backprop_runtime_boxplots_{preset}.png", dpi=300)
    plt.close(fig)




def main():
    parser = argparse.ArgumentParser(
        description="Visualise GPU backprop benchmark results.")
    parser.add_argument("-p",
                        "--preset",
                        choices=["S", "M", "L", "paper"],
                        default="S",
                        help="Benchmark preset to plot.")
    parser.add_argument("-o",
                        "--output-dir",
                        default="ad_plots",
                        help="Directory for generated figures.")
    parser.add_argument("-f",
                        "--frameworks",
                        nargs="+",
                        default=["jax_cpu","jax_gpu", "pytorch_cpu", "pytorch_gpu"],
                        help="Frameworks to include in the plots.")
    parser.add_argument("-b",
                        "--baseline",
                        default="jax_cpu",
                        help="Framework to use as baseline for ratio plots.")
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    labels = load_benchmark_labels(Path("bench_info"))
    frameworks = args.frameworks
    if args.baseline not in frameworks:
        raise SystemExit("Baseline framework must be part of --frameworks.")
    raw_results = fetch_results(args.preset, frameworks)
    if raw_results.empty:
        raise SystemExit("No benchmark results found for the requested preset.")
    medians, filtered = select_best_runs(raw_results)
    plot_speedup_heatmap(medians, labels, frameworks, args.baseline, args.preset,
                         output_dir)
    plot_runtime_bars(medians, labels, frameworks, args.preset, output_dir)
    plot_speedup_bars(medians, labels, frameworks, args.baseline, args.preset,
                      output_dir)
    # plot_runtime_boxplots(filtered, frameworks, args.preset, output_dir)


if __name__ == "__main__":
    main()
