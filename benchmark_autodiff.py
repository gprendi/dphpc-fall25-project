import argparse
import pathlib
import json
from npbench.infrastructure import Benchmark, generate_framework, LineCount, Test

def discover_autodiff_benchmarks(bench_info_dir):
    benches = []
    for path in sorted(bench_info_dir.glob("*.json")):
        with path.open() as fh:
            try:
                data = json.load(fh)
            except json.JSONDecodeError:
                continue
        bench = data.get("benchmark", {})
        if "autodiff" not in bench:
            continue
        benches.append(path.stem)
    return benches

def run_all(bench_info_dir, frameworks, sizes, repeats, modes, validate, timeout):
    benches = discover_autodiff_benchmarks(bench_info_dir)
    if not benches:
        print("No autodiff-enabled benchmarks found.")
        return

    for mode in modes:
        for fw in frameworks:
            for size, repeat in zip(sizes, repeats):
                print(f"==== Benchmarking {fw} size {size} ({repeat} runs) mode: {mode} ====")
                for bench_id in benches:
                    print(f">>> Running {bench_id}...")
                    bench = Benchmark(bench_id)
                    frmwrk = generate_framework(fw)
                    numpy = generate_framework("numpy")
                    jax = generate_framework("jax")
                    lcount = LineCount(bench, frmwrk, numpy)
                    lcount.count()
                    # lcount_jax = LineCount(bench, frmwrk, jax)
                    # lcount_jax.count()
                    if mode == "backward":
                        test = Test(bench, frmwrk, numpy, jax)
                    else:
                        test = Test(bench, frmwrk, numpy)
                    test.run(size, validate, repeat, timeout, mode=mode)
                    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frameworks", nargs="+", default=["pytorch_cpu", "pytorch_gpu", "jax"],
                        help="List of frameworks to benchmark")
    parser.add_argument("--sizes", nargs="+", default=["S", "M", "L"],
                        help="List of sizes to benchmark")
    parser.add_argument("--repeats", nargs="+", type=int, default=[20, 10, 10],
                        help="Number of repeats for each size")
    parser.add_argument("--modes", nargs="+", default=["backward", "forward"],
                        help="Modes to run (backward, forward)")
    parser.add_argument("--validate", type=bool, default=False,
                        help="Whether to validate results")
    parser.add_argument("--timeout", type=float, default=2000.0,
                        help="Timeout for each benchmark")
    parser.add_argument("--bench-info-dir", type=str, default="bench_info",
                        help="Directory containing benchmark info JSONs")
    args = parser.parse_args()

    repo_root = pathlib.Path(__file__).parent.resolve()
    bench_info_dir = repo_root / args.bench_info_dir

    run_all(
        bench_info_dir=bench_info_dir,
        frameworks=args.frameworks,
        sizes=args.sizes,
        repeats=args.repeats,
        modes=args.modes,
        validate=args.validate,
        timeout=args.timeout
    )
