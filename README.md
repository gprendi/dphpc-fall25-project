Autodiff benchmarking for NPBench
==================================

This repository starts from the NPBench project and keeps its data model and benchmark collection. For standard NPBench usage (framework matrix, quickstart, publication details), please refer to the upstream repo: https://github.com/spcl/npbench. The notes below focus only on the additions we made for reverse‑mode AD benchmarking of JAX and PyTorch plus the small helper scripts around databases and plotting.

The work was completed in the context of ETH Zürich’s Design of Parallel and High-Performance Computing (DPHPC) course in 2025. The presentation (`DPHPC_JAXvsPyTorchAD.pdf`) in the repo walks through key results and takeaways of this project.

Setup
-----
- Python 3.12+. Install dependencies and the local NPBench package:
  ```
  python -m pip install -r requirements.txt
  python -m pip install -e .
  ```
- GPU runs assume matching CUDA/CuDNN builds of JAX and PyTorch.

Running backprop benchmarks
---------------------------
- Discover kernels that define autodiff metadata:
  ```
  python benchmark_backprop.py --list-benchmarks
  ```
- Run forward + backward for one kernel/framework (defaults: all autodiff kernels, jax/pytorch CPU+GPU, modes = forward+backward, preset S):
  ```
  python benchmark_backprop.py -b gemm -f pytorch_gpu -m backward -p L -r 5 --timeout 400
  ```
  Useful flags: `--validate false` to skip correctness checks, `--baseline-framework jax_cpu` to pick the backward validator, `--strict-frameworks` to abort on missing frameworks.
- Batch helper: `./scripts/run_autodiff_backprop.sh -f pytorch_gpu -p S` (uses `uv run` under the hood and walks all autodiff-enabled kernels in both forward and backward mode).
- Outputs land in the standard NPBench SQLite database `npbench.db` with both timing results and line counts.

Managing result databases
-------------------------
- Export a DB (tables -> CSV) to `dbs/exports/`:
  ```
  python dbs/export_db_to_csv.py
  ```
- Merge two NPBench-format DBs into a fresh file:
  ```
  python dbs/merge_dbs.py dbs/linear_algebra.db dbs/pat1M_gpu.db dbs/combined.db --overwrite
  ```
- The repo also ships several precomputed `.db` files under `dbs/` for convenience when plotting.

Plotting
--------
- Generate the main backward/forward plots (heatmap + stacked bars) from `npbench.db`:
  ```
  python plotting/plot_backprop_results.py -p L -f jax_cpu jax_gpu pytorch_cpu pytorch_gpu -o ad_plots
  ```
  Pass `-k` to focus on specific kernels or multiple `-p` values to mix presets per kernel.
- Additional figure scripts live in `plotting/` for report-specific visuals (heatmaps, unroll sweeps, paper LU/Cholesky). Each script documents its own flags; they all read NPBench-format SQLite DBs.

Notes on upstream NPBench
-------------------------
- Benchmark definitions live in `bench_info/`; framework metadata in `framework_info/`.
- You can still run the original NPBench harness via `scripts/run_benchmark.py` or `scripts/run_framework.py`. See the upstream README for full details and publication references.
