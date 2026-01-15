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

EXEC_MODES = ("forward", "backward")
PRESET = "paper"

# Use a serif face for publication-ready plots and larger text.
rcParams["font.family"] = "Nimbus Roman"
rcParams["font.size"] = 16
rcParams["axes.titlesize"] = 22
rcParams["axes.labelsize"] = 18
rcParams["xtick.labelsize"] = 18
rcParams["ytick.labelsize"] = 20

# (db_path, framework_in_db, alias_for_plot)
DATA_CONFIG = [
    ("dbs/lu_1_cpu.db", "jax_cpu", "jax1"),
    ("dbs/lu_1_cpu.db", "pytorch_cpu", "pytorch1"),
    ("dbs/lu_2_cpu.db", "pytorch_cpu", "pytorch2"),
    ("dbs/lu_3_cpu.db", "jax_cpu", "jax3"),
    ("dbs/lu_3_cpu.db", "pytorch_cpu", "pytorch3"),
    ("dbs/chol_1_cpu.db", "jax_cpu", "jax1"),
    ("dbs/chol_1_cpu.db", "pytorch_cpu", "pytorch1"),
    ("dbs/chol_2_cpu.db", "pytorch_cpu", "pytorch2"),
    ("dbs/chol_3_cpu.db", "jax_cpu", "jax3"),
    ("dbs/chol_3_cpu.db", "pytorch_cpu", "pytorch3"),
]

FRAMEWORK_DISPLAY = {
    "jax1": "JAX",
    "pytorch1": "PyTorch",
    "pytorch2": "PyTorch",
    "jax3": "JAX",
    "pytorch3": "PyTorch",
}

BENCHMARKS = ["lu", "cholesky", "cholesky2"]


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
                                  lambda s: np.median(
                                      np.abs(s - np.median(s))))
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
    desired_order = ["cholesky", "lu"]
    benches = [b for b in desired_order if b in benches]
    bench_labels = ["lu", "cholesky"][:len(benches)]
    mad_lookup = medians.set_index(["benchmark", "framework", "mode"])["mad_pct"]

    ratio_tables = {}
    baseline_times = {}
    for mode in EXEC_MODES:
        base = pivot.get((baseline, mode), pd.Series(dtype=float)).reindex(benches)
        ratios = {}
        for framework in frameworks:
            series = pivot.get((framework, mode), pd.Series(dtype=float)).reindex(benches)
            ratios[framework] = base / series
        ratio_tables[mode] = pd.DataFrame(ratios, index=benches)
        baseline_times[mode] = base

    blocks = [
        ["jax1", "pytorch1"],
        ["pytorch2"],
        ["jax3", "pytorch3"],
    ]
    norm = LogNorm(vmin=0.5, vmax=2.0)

    def _plot_single(mode: str, df: pd.DataFrame, base_times: pd.Series):
        total_cols = sum(len(b) for b in blocks)
        fig_width = max(8, total_cols * 1.2)
        fig_height = 3


        fig, axes = plt.subplots(
            1, len(blocks),
            figsize=(fig_width, fig_height),
            gridspec_kw={"width_ratios": [len(b) for b in blocks]}
        )
        if len(blocks) == 1:
            axes = [axes]

        fig.subplots_adjust(left=0.12, right=0.85, top=0.9, bottom=0.2, wspace=-2)
        im = None
        for ax_idx, block in enumerate(blocks):
            sub_df = df[block]
            ax = axes[ax_idx]
            im = ax.imshow(
                sub_df.to_numpy(),
                cmap="RdYlGn",
                norm=norm,   # log scale
                aspect="auto"
            )

            positions = np.arange(len(benches))
            if ax_idx == 0:
                ax.set_yticks(positions)
                ax.set_yticklabels(bench_labels, rotation=40, ha="right", va="center")
            else:
                ax.set_yticks(positions)
                ax.tick_params(labelleft=False)

            ax.set_xticks(np.arange(len(block)))
            ax.set_xticklabels(
                [FRAMEWORK_DISPLAY.get(fw, fw) for fw in block],
                rotation=40, ha="right"
            )

            for i, bench in enumerate(benches):
                for j, framework in enumerate(block):
                    value = sub_df.iloc[i, j]
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

            if ax_idx == 0:
                ax.set_title(f"Naive")
            elif ax_idx == 1:
                ax.set_title(f"Subroutine")
            elif ax_idx == 2:
                ax.set_title(f"Library")
        cax = fig.add_axes([0.858, 0.355, 0.015, 0.47])
        fig.colorbar(im, cax=cax)
        plt.tight_layout(rect=[0.1, 0, 0.858, 1])
        filename = f"sh_{mode}_{preset}_lu_chol.{output_format}"
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    _plot_single("backward", ratio_tables["backward"], baseline_times["backward"])


def fetch_data() -> pd.DataFrame:
    frames = []
    placeholders = ",".join("?" for _ in BENCHMARKS)
    query = f"""
        SELECT benchmark, framework, mode, details, time, preset
        FROM results
        WHERE benchmark IN ({placeholders})
          AND framework = ?
          AND preset = ?
          AND mode IN ('forward', 'backward')
    """
    for db_path, framework_db, alias in DATA_CONFIG:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(query, conn, params=(*BENCHMARKS, framework_db, PRESET))
        conn.close()
        if df.empty:
            continue
        # DB3 stores cholesky2; treat it as cholesky for this plot.
        df = df[~df["details"].str.contains("lib-implementation", na=False)]
        df["benchmark"] = df["benchmark"].replace({"cholesky2": "cholesky"})
        df["framework"] = alias  # rename for plotting column
        frames.append(df)
    if not frames:
        raise SystemExit("No data found in the configured databases.")
    return pd.concat(frames, ignore_index=True)


def main():
    parser = argparse.ArgumentParser(
        description="Plot LU/Cholesky speedup heatmaps for the paper."
    )
    parser.add_argument("-o",
                        "--output-dir",
                        default="ad_plots",
                        help="Directory for generated figures.")
    parser.add_argument("--format",
                        default="eps",
                        choices=["png", "eps", "pdf", "svg"],
                        help="Output figure format/extension.")
    parser.add_argument("-b",
                        "--baseline",
                        default="jax1",
                        choices=["jax1", "pytorch1", "pytorch2", "jax3", "pytorch3"],
                        help="Baseline framework alias used for ratios.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = load_benchmark_labels(Path("bench_info"))
    labels = {k: v for k, v in labels.items() if k in BENCHMARKS}

    raw = fetch_data()
    medians, _ = select_best_runs(raw)

    frameworks = ["jax1", "pytorch1", "pytorch2", "jax3", "pytorch3"]
    if args.baseline not in frameworks:
        raise SystemExit("Baseline framework must be part of the configured frameworks.")
    plot_speedup_heatmap(
        medians,
        labels,
        frameworks,
        args.baseline,
        PRESET,
        output_dir,
        output_format=args.format,
    )


if __name__ == "__main__":
    main()
