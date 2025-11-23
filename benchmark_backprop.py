import argparse
import json
from multiprocessing import Process, set_start_method
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

DEFAULT_FRAMEWORKS: Tuple[str, ...] = ("jax_cpu", "jax_gpu", "pytorch_cpu", "pytorch_gpu")
DEFAULT_MODES: Tuple[str, ...] = ("backward", )#, "forward")
# Kernels with PyTorch autodiff implementations; serves as default bench set.
DEFAULT_BENCHMARKS: Tuple[str, ...] = (
    "go_fast",
    "heat_3d",
    "fdtd_2d",
    # "k2mm",
    # "k3mm",
    # "atax",
    # "go_fast",
    # "gemm",
    # "gemver",
    # "gesummv",
    # "mvt",
    # "symm", -> torch loop
    # "syr2k",
    # "syrk",
    # "trmm",
    # "cholesky2",
    # "compute",
    # "doitgen",
    # "hdiff",
    # "jacobi_1d",
    # "seidel_2d",
    # "softmax",
)

try:
    set_start_method("spawn")
except RuntimeError:
    pass


def _str2bool(value):
    if isinstance(value, bool):
        return value
    lowered = value.lower()
    if lowered in ('yes', 'true', 't', 'y', '1'):
        return True
    if lowered in ('no', 'false', 'f', 'n', '0'):
        return False
    raise argparse.ArgumentTypeError('Boolean value expected.')


def _discover_autodiff_benchmarks(bench_dir: Path) -> Dict[str, Dict[str, str]]:
    """Return benchmarks that define autodiff metadata."""
    benches: Dict[str, Dict[str, str]] = {}
    for path in sorted(bench_dir.glob("*.json")):
        try:
            with path.open() as fh:
                payload = json.load(fh)
        except json.JSONDecodeError as exc:
            print(f"Warning: failed to parse {path.name}: {exc}")
            continue
        bench = payload.get("benchmark", {})
        if "autodiff" not in bench:
            continue
        benches[path.stem] = {
            "name": bench.get("name", path.stem),
            "short_name": bench.get("short_name", path.stem),
        }
    return benches


def _unique(seq: Iterable[str]) -> List[str]:
    seen = set()
    unique_items: List[str] = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items


def _validate_frameworks(
        names: Sequence[str],
        strict: bool) -> Tuple[List[str], List[Tuple[str, str]]]:
    """Return available frameworks and the ones skipped due to errors."""
    from npbench.infrastructure import generate_framework

    available: List[str] = []
    skipped: List[Tuple[str, str]] = []
    for fname in _unique(names):
        try:
            generate_framework(fname)
        except Exception as exc:
            skipped.append((fname, str(exc)))
            if strict:
                raise RuntimeError(
                    f"Failed to initialise framework '{fname}': {exc}") from exc
        else:
            available.append(fname)
    return available, skipped


def _run_combo(benchname: str, framework_name: str, preset: str, validate: bool,
               repeat: int, timeout: float, ignore_errors: bool,
               modes: Sequence[str], baseline_framework: Optional[str],
               warmup: int) -> None:
    """Execute a benchmark/framework pair for every requested mode."""
    from npbench.infrastructure import (Benchmark, LineCount, Test,
                                        generate_framework)

    bench = Benchmark(benchname)
    frmwrk = generate_framework(framework_name)
    numpy = generate_framework("numpy")
    baseline = None
    needs_baseline = "backward" in modes and validate and baseline_framework
    if needs_baseline:
        assert baseline_framework is not None
        baseline = generate_framework(baseline_framework)

    lcount = LineCount(bench, frmwrk, numpy)
    lcount.count()

    for mode in modes:
        if mode == "backward":
            test = Test(bench, frmwrk, numpy, baseline)
        else:
            test = Test(bench, frmwrk, numpy)
        test.run(preset,
                 validate,
                 repeat,
                 timeout,
                 ignore_errors,
                 mode=mode,
                 warmup=warmup)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run forward and backward NPBench autodiff benchmarks.")
    parser.add_argument("-b",
                        "--benchmarks",
                        nargs="+",
                        help="Specific benchmarks to run (bench_info IDs).")
    parser.add_argument("-f",
                        "--frameworks",
                        nargs="+",
                        help="Framework names to benchmark.")
    parser.add_argument("-p",
                        "--preset",
                        choices=['S', 'M', 'L', 'paper'],
                        default='S',
                        help="NPBench preset to use.")
    parser.add_argument("-r",
                        "--repeat",
                        type=int,
                        default=5,
                        help="Number of repetitions per benchmark run.")
    parser.add_argument("-w",
                        "--warmup",
                        type=int,
                        default=2,
                        help="Number of warm-up executions before timing.")
    parser.add_argument("-t",
                        "--timeout",
                        type=float,
                        default=200.0,
                        help="Timeout (seconds) for each benchmark execution.")
    parser.add_argument("-m",
                        "--modes",
                        nargs="+",
                        choices=list(DEFAULT_MODES),
                        help="Execution modes to run in order.",
                        default=None)
    parser.add_argument("-v",
                        "--validate",
                        type=_str2bool,
                        default=True,
                        help="Validate outputs (forward via NumPy, backward via JAX).")
    parser.add_argument("--ignore-errors",
                        type=_str2bool,
                        default=False,
                        help="Skip individual implementation failures.")
    parser.add_argument("--baseline-framework",
                        default="jax_cpu",
                        help="Framework used for backward validation.")
    parser.add_argument("--allow-gpu-baseline",
                        action="store_true",
                        help="Allow GPU-based baseline frameworks (defaults to CPU to avoid OOM).")
    parser.add_argument("--bench-info-dir",
                        default="bench_info",
                        help="Directory containing benchmark metadata JSON files.")
    parser.add_argument("--list-benchmarks",
                        action="store_true",
                        help="List autodiff-enabled benchmarks and exit.")
    parser.add_argument("--strict-frameworks",
                        action="store_true",
                        help="Abort if a framework fails to initialise.")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if (not args.allow_gpu_baseline
            and args.baseline_framework.lower().endswith("_gpu")):
        candidate = args.baseline_framework[:-4] + "_cpu"
        print(
            f"GPU baselines are disabled by default, switching baseline framework "
            f"from '{args.baseline_framework}' to '{candidate}'. "
            "Use --allow-gpu-baseline to override."
        )
        args.baseline_framework = candidate
    bench_dir = Path(args.bench_info_dir)
    if not bench_dir.is_dir():
        print(f"Benchmark info directory '{bench_dir}' does not exist.")
        return 1

    bench_map = _discover_autodiff_benchmarks(bench_dir)
    if not bench_map:
        print(f"No autodiff-enabled benchmarks found in '{bench_dir}'.")
        return 1

    if args.list_benchmarks:
        print("Autodiff-enabled benchmarks:")
        for name, meta in bench_map.items():
            print(f" - {name}: {meta['name']} (short: {meta['short_name']})")
        return 0

    bench_selection: Sequence[str]
    if args.benchmarks:
        bench_selection = args.benchmarks
    else:
        bench_selection = [
            bench for bench in DEFAULT_BENCHMARKS if bench in bench_map
        ]
        missing_defaults = [
            bench for bench in DEFAULT_BENCHMARKS if bench not in bench_map
        ]
        if missing_defaults:
            print(
                "Warning: the following default benchmarks are unavailable and "
                f"will be skipped: {', '.join(missing_defaults)}")
        if not bench_selection:
            print("No default benchmarks available; falling back to all.")
            bench_selection = list(bench_map.keys())
    requested_benches = _unique(bench_selection)
    missing = [b for b in requested_benches if b not in bench_map]
    if missing:
        print(
            f"Invalid benchmark IDs (not autodiff-enabled or missing): {', '.join(missing)}"
        )
        return 1
    bench_list = requested_benches

    frameworks = _unique(args.frameworks or list(DEFAULT_FRAMEWORKS))
    frameworks, skipped = _validate_frameworks(frameworks,
                                               args.strict_frameworks)
    if skipped and not args.strict_frameworks:
        print("Skipping frameworks that failed to initialise:")
        for fname, reason in skipped:
            print(f" - {fname}: {reason}")
    if not frameworks:
        print("No frameworks available to benchmark.")
        return 1

    modes = tuple(_unique(args.modes or list(DEFAULT_MODES)))
    baseline_framework: Optional[str]
    if "backward" in modes and args.validate:
        from npbench.infrastructure import generate_framework

        baseline_framework = args.baseline_framework
        try:
            baseline_check = generate_framework(baseline_framework)
        except Exception as exc:
            raise RuntimeError(
                f"Failed to initialise backward baseline '{baseline_framework}'."
            ) from exc
        else:
            del baseline_check
    else:
        baseline_framework = None

    print("Benchmarks:", ", ".join(bench_list))
    print("Frameworks:", ", ".join(frameworks))
    print("Modes:", ", ".join(modes))

    failures: List[Tuple[str, str]] = []
    try:
        for benchname in bench_list:
            for framework in frameworks:
                print(
                    f"\n>>> Running {benchname} on {framework} ({', '.join(modes)})"
                )
                process = Process(target=_run_combo,
                                  args=(benchname, framework, args.preset,
                                        args.validate, args.repeat,
                                        args.timeout, args.ignore_errors,
                                        modes, baseline_framework,
                                        args.warmup))
                process.start()
                process.join()
                if process.exitcode != 0:
                    failures.append((benchname, framework))
    except KeyboardInterrupt:
        print("\nBenchmarking interrupted by user.")
        return 130

    if failures:
        print("\nFailed combinations:")
        for benchname, framework in failures:
            print(f" - {benchname} / {framework}")
        return 1

    print("\nAll requested benchmarks completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
