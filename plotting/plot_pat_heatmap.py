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
    "jax_gpu": "JAX GPU",
    "torch_gpu_nocompile": "PyTorch GPU (no compile)",
    "torch_gpu_compile": "PyTorch GPU (compiled)",
    "jax_cpu": "JAX CPU",
    "torch_cpu_nocompile": "PyTorch CPU (no compile)",
    "torch_cpu_compile": "PyTorch CPU (compiled)",
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

    def _plot_single(mode: str, df: pd.DataFrame, runtime_map: Dict[str, pd.Series]):
        fig_width = max(6, len(frameworks) * 1.4)
        fig_height = max(4, len(benches) * 0.5)

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))

        im = ax.imshow(
            df.to_numpy(),
            cmap="RdYlGn",
            norm=LogNorm(vmin=0.5, vmax=2.0),
            aspect="auto"
        )

        ax.set_yticks(np.arange(len(benches)))
        ax.set_yticklabels([labels.get(b, b) for b in benches])
        ax.set_xticks(np.arange(len(frameworks)))
        ax.set_xticklabels(
            [FRAMEWORK_DISPLAY.get(fw, fw.replace("_", " ").title()) for fw in frameworks],
            rotation=30, ha="right"
        )

        for i, bench in enumerate(benches):
            for j, framework in enumerate(frameworks):
                value = df.iloc[i, j]
                label = my_speedup_abbr(value)
                base_fw = BASELINE_MAP.get(framework, baseline)
                if framework == base_fw:
                    series = runtime_map.get(framework)
                    runtime_ms = math.nan
                    if series is not None and len(series) > i:
                        runtime_ms = series.iloc[i]
                    label = ""
                    if not math.isnan(runtime_ms):
                        label = my_runtime_abbr(runtime_ms / 1000.0)
                ax.text(
                    j, i, label,
                    ha="center", va="center", color="black"
                )

        fig.tight_layout()
        filename = f"sh_{mode}_{preset}_{'_'.join(benches)}.png"
        fig.savefig(output_dir / filename, dpi=300)
        plt.close(fig)

    _plot_single("forward", ratio_tables["forward"], runtime_tables["forward"])
    _plot_single("backward", ratio_tables["backward"], runtime_tables["backward"])


def fetch_data() -> pd.DataFrame:
    frames = []
    placeholders = ",".join("?" for _ in BENCHMARKS)
    query = f"""
        SELECT benchmark, framework, mode, details, time, preset
        FROM results
        WHERE benchmark IN ({placeholders})
          AND framework = ?
          AND mode IN ('forward', 'backward')
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
    output_dir = Path("ad_plots")
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = load_benchmark_labels(Path("bench_info"))
    labels = {k: v for k, v in labels.items() if k in BENCHMARKS}

    raw = fetch_data()
    medians, _ = select_best_runs(raw)

    frameworks = [cfg[2] for cfg in DATA_CONFIG]
    preset_label = "pat1M"
    plot_speedup_heatmap(medians, labels, frameworks, "jax_cpu", preset_label,
                         output_dir)


if __name__ == "__main__":
    main()
