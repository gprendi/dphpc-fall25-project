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

# Plot only backward mode for this report.
EXEC_MODES = ("backward",)

DATA_CONFIG = [
    # (db_path, framework_in_db, alias_for_plot)
    ("dbs/pat1M_nocompiled_gpu.db", "jax_gpu", "jax_gpu"),
    ("dbs/pat1M_nocompiled_gpu.db", "pytorch_gpu", "torch_gpu_nocompile"),
    ("dbs/pat1M_compiled_gpu.db", "pytorch_gpu", "torch_gpu_compile"),
    ("dbs/pat1M_nocompiled_cpu.db", "jax_cpu", "jax_cpu"),  # baseline
    ("dbs/pat1M_nocompiled_cpu.db", "pytorch_cpu", "torch_cpu_nocompile"),
    ("dbs/pat1M_compiled_cpu.db", "pytorch_cpu", "torch_cpu_compile"),
]

FRAMEWORK_DISPLAY = {
    "jax_gpu": "JAX",
    "torch_gpu_nocompile": "PyTorch\n(not compiled)",
    "torch_gpu_compile": "PyTorch\n(compiled)",
    "jax_cpu": "JAX",
    "torch_cpu_nocompile": "PyTorch\n(not compiled)",
    "torch_cpu_compile": "PyTorch\n(compiled)",
}

BASELINE_MAP = {
    "jax_gpu": "jax_gpu",
    "torch_gpu_nocompile": "jax_gpu",
    "torch_gpu_compile": "jax_gpu",
    "jax_cpu": "jax_cpu",
    "torch_cpu_nocompile": "jax_cpu",
    "torch_cpu_compile": "jax_cpu",
}

BENCHMARKS = ["npgofast", "correlat"]  # go_fast and correlation short names


# Use a serif face for publication-ready plots and larger text.
rcParams["font.family"] = "Nimbus Roman"
rcParams["font.size"] = 18
rcParams["axes.titlesize"] = 22
rcParams["axes.labelsize"] = 18
rcParams["xtick.labelsize"] = 18
rcParams["ytick.labelsize"] = 20


def _filename(prefix: str, mode: str, preset: str, benches: List[str],
              ext: str = "png") -> str:
    kernels = "_".join(benches) if benches else "all"
    parts = [prefix, mode, preset, kernels]
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
        labels[short_name] = bench.get("name", short_name)
    return labels


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
                         output_dir: Path, output_format: str = "png"):

    pivot = _pivot_times(medians)
    benches = _ordered_benchmarks(medians, labels)
    bench_labels = [labels.get(b, b) for b in benches]
    mad_lookup = medians.set_index(["benchmark", "framework", "mode"])["mad_pct"]

    ratio_tables = {}
    runtime_tables = {}
    for mode in EXEC_MODES:
        ratios = {}
        runtime_tables[mode] = {}
        for framework in frameworks:
            base_fw = BASELINE_MAP.get(framework, baseline)
            base_series = pivot[(base_fw, mode)].reindex(benches)
            target_series = pivot[(framework, mode)].reindex(benches)
            ratios[framework] = base_series / target_series
            if framework == base_fw:
                runtime_tables[mode][framework] = target_series
        ratio_tables[mode] = pd.DataFrame(ratios).reindex(benches)

    norm = LogNorm(vmin=0.5, vmax=2.0)

    def _render_heatmap(ax, mode: str, df: pd.DataFrame,
                        runtime_map: Dict[str, pd.Series]):
        im = ax.imshow(
            df.to_numpy(),
            cmap="RdYlGn",
            norm=norm,
            aspect="auto"
        )

        ax.set_yticks(np.arange(len(benches)))
        ax.set_yticklabels(bench_labels, rotation=40, ha="right", va="center")
        ax.set_xticks(np.arange(len(frameworks)))
        ax.set_xticklabels(
            [FRAMEWORK_DISPLAY.get(fw, fw.replace("_", " ").title()) for fw in frameworks],
            rotation=35, ha="right"
        )
        ax.tick_params(axis="x", rotation=35)
        # Nudge x tick labels slightly to the right for better visual centering.
        for lbl in ax.get_xticklabels():
            lbl.set_rotation_mode("anchor")
            x, y = lbl.get_position()
            lbl.set_x(x + 0.2)

        # Group headers for GPU (left) and CPU (right) columns.
        n_fw = len(frameworks)
        if n_fw > 1:
            group_defs = [("Backward Speedup GPU", 0, 3),
                          ("Backward Speedup CPU", 3, n_fw)]
            for label, start, end in group_defs:
                start = max(start, 0)
                end = min(end, n_fw)
                if start >= end:
                    continue
                # Center the header above the spanned columns.
                mid_col = (start + end - 1) / 2
                center = mid_col / (n_fw - 1)
                ax.text(center,
                        1.05,
                        label,
                        transform=ax.transAxes,
                        ha="center",
                        va="bottom")

        for i, bench in enumerate(benches):
            for j, framework in enumerate(frameworks):
                value = df.iloc[i, j]
                label = my_speedup_abbr(value)
                base_fw = BASELINE_MAP.get(framework, baseline)
                suffix = my_mad_superscript(
                    mad_lookup.get((bench, framework, mode), math.nan)
                )
                if framework == base_fw:
                    series = runtime_map.get(framework)
                    runtime_ms = math.nan
                    if series is not None and len(series) > i:
                        runtime_ms = series.iloc[i]
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

    def _plot_single(mode: str, df: pd.DataFrame, runtime_map: Dict[str, pd.Series]):
        fig_width = max(8, len(frameworks) * 1.5)
        fig_height = max(4, len(benches) * 0.45)

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        fig.subplots_adjust(left=0.2, right=0.88, top=0.86, bottom=0.18)
        im = _render_heatmap(ax, mode, df, runtime_map)

        cax = fig.add_axes([0.87, 0.41, 0.015, 0.43])
        fig.colorbar(im, cax=cax)
        plt.tight_layout(rect=[0, 0, 0.89, 1])

        filename = _filename("sh", mode, preset, benches, ext=output_format)
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    _plot_single("backward", ratio_tables["backward"], runtime_tables["backward"])


def fetch_data() -> pd.DataFrame:
    frames = []
    placeholders = ",".join("?" for _ in BENCHMARKS)
    query = f"""
        SELECT benchmark, framework, mode, details, time, preset
        FROM results
        WHERE benchmark IN ({placeholders})
          AND framework = ?
          AND mode IN ('backward')
    """
    for db_path, db_framework, alias in DATA_CONFIG:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(query, conn, params=(*BENCHMARKS, db_framework))
        conn.close()
        if df.empty:
            continue
        # Drop auxiliary JAX lib implementations; we want only the main runs
        df = df[~df["details"].str.contains("lib-implementation", na=False)]
        df["framework"] = alias  # rename for plotting column
        frames.append(df)
    if not frames:
        raise SystemExit("No data found in the configured databases.")
    return pd.concat(frames, ignore_index=True)


def main():
    parser = argparse.ArgumentParser(
        description="Visualise PAT heatmap benchmark results.")
    parser.add_argument("-o",
                        "--output-dir",
                        default="ad_plots",
                        help="Directory for generated figures.")
    parser.add_argument("--format",
                        default="eps",
                        choices=["png", "eps", "pdf", "svg"],
                        help="Output figure format/extension.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = load_benchmark_labels(Path("bench_info"))
    labels = {k: v for k, v in labels.items() if k in BENCHMARKS}

    raw = fetch_data()
    medians, _ = select_best_runs(raw)

    frameworks = [cfg[2] for cfg in DATA_CONFIG]
    preset_label = "pat1M"
    plot_speedup_heatmap(medians, labels, frameworks, "jax_cpu", preset_label,
                         output_dir, output_format=args.format)


if __name__ == "__main__":
    main()
