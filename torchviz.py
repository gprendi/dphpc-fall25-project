import argparse
from npbench.infrastructure import Benchmark, Test
# import 
# def load_kernel(module_name, func_name):
#     return getattr(importlib.import_module(module_name), func_name)

# kernel = load_kernel("npbench.benchmarks.polybench.jacobi_1d.jacobi_1d_pytorch")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b",
                        "--benchname",
                        type=str,
                        nargs=1,
                        default="jacobi_1d")
    args = vars(parser.parse_args())

    info = Benchmark(args["benchname"])