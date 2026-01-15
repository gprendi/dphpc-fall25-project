import json
import math
import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import pandas as pd

EXEC_MODES = ("forward", "backward")
PRESET = "paper"

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
    return f"{ms} ms"


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

    def _plot_single(mode: str, df: pd.DataFrame, base_times: pd.Series):
        total_cols = sum(len(b) for b in blocks)
        fig_width = max(8, total_cols * 1.2)
        fig_height = max(4, len(benches) * 0.5)

        fig, axes = plt.subplots(
            1, len(blocks),
            figsize=(fig_width, fig_height),
            sharey=True,
            gridspec_kw={"width_ratios": [len(b) for b in blocks]}
        )
        if len(blocks) == 1:
            axes = [axes]

        for ax_idx, block in enumerate(blocks):
            sub_df = df[block]
            ax = axes[ax_idx]
            ax.imshow(
                sub_df.to_numpy(),
                cmap="RdYlGn",
                norm=LogNorm(vmin=0.5, vmax=2.0),
                aspect="auto"
            )

            if ax_idx == 0:
                ax.set_yticks(np.arange(len(benches)))
                ax.set_yticklabels([labels.get(b, b) for b in benches])
            else:
                ax.set_yticks(np.arange(len(benches)))
                ax.set_yticklabels([])

            ax.set_xticks(np.arange(len(block)))
            ax.set_xticklabels(
                [FRAMEWORK_DISPLAY.get(fw, fw) for fw in block],
                rotation=30, ha="right"
            )

            for i, bench in enumerate(benches):
                for j, framework in enumerate(block):
                    value = sub_df.iloc[i, j]
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

            if ax_idx == 0:
                ax.set_title(f"Naive")
            elif ax_idx == 1:
                ax.set_title(f"Subroutine")
            elif ax_idx == 2:
                ax.set_title(f"Lib-call")
            
        fig.tight_layout()
        filename = f"sh_{mode}_{preset}_lu_chol.png"
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    _plot_single("forward", ratio_tables["forward"], baseline_times["forward"])
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
    output_dir = Path("ad_plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = load_benchmark_labels(Path("bench_info"))
    labels = {k: v for k, v in labels.items() if k in BENCHMARKS}

    raw = fetch_data()
    medians, _ = select_best_runs(raw)

    frameworks = ["jax1", "pytorch1", "pytorch2", "jax3", "pytorch3"]
    plot_speedup_heatmap(medians, labels, frameworks, "jax1", PRESET, output_dir)


if __name__ == "__main__":
    main()
