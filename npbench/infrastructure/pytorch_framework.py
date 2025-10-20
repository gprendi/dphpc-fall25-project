from npbench.infrastructure import Benchmark, Framework
from typing import Any, Callable, Dict
import pathlib

_impl = {
}

class PytorchFramework(Framework):

    """ A class for reading and processing framework information. """
    def __init__(self, fname: str):
        """ Reads framework information.
        :param fname: The framework name.
        """

        super().__init__(fname)

    def version(self) -> str:
        return "v0.1"

    def impl_files(self, bench: Benchmark):
        """ Returns the framework's implementation files for a particular
        benchmark.
        :param bench: A benchmark.
        :returns: A list of the benchmark implementation files.
        """

        parent_folder = pathlib.Path(__file__).parent.absolute()
        implementations = []

        # appending the default implementation
        pymod_path = parent_folder.joinpath("..", "..", "npbench", "benchmarks", bench.info["relative_path"],
                                            bench.info["module_name"] + "_" + self.info["postfix"] + ".py")

        implementations.append((pymod_path, 'default'))

        for impl_name, impl_postfix in _impl.items():
            pymod_path = parent_folder.joinpath(
                "..", "..", "npbench", "benchmarks", bench.info["relative_path"],
                bench.info["module_name"] + "_" + self.info["postfix"] + "_" + impl_postfix + ".py")
            implementations.append((pymod_path, impl_name))

        return implementations

    def implementations(self, bench: Benchmark):
        """ Returns the framework's implementations for a particular benchmark.
        :param bench: A benchmark.
        :returns: A list of the benchmark implementations.
        """

        module_pypath = "npbench.benchmarks.{r}.{m}".format(r=bench.info["relative_path"].replace('/', '.'),
                                                            m=bench.info["module_name"])
        if "postfix" in self.info.keys():
            postfix = self.info["postfix"]
        else:
            postfix = self.fname
        module_str = "{m}_{p}".format(m=module_pypath, p=postfix)
        func_str = bench.info["func_name"]

        implementations = []

        # appending the default implementation
        try:
            ldict = dict()
            exec("from {m} import {f} as impl".format(m=module_str, f=func_str), ldict)
            implementations.append((ldict['impl'], 'default'))
        except Exception as e:
            print("Failed to load the {r} {f} implementation.".format(r=self.info["full_name"], f=func_str))
            raise e

        for impl_name, impl_postfix in _impl.items():
            ldict = dict()
            try:
                exec("from {m}_{p} import {f} as impl".format(m=module_str, p=impl_postfix, f=func_str), ldict)
                implementations.append((ldict['impl'], impl_name))
            except ImportError:
                continue
            except Exception:
                print("Failed to load the {r} {f} implementation.".format(r=self.info["full_name"], f=impl_name))
                continue

        return implementations

    def copy_func(self) -> Callable:
        import torch
        torch.set_default_device('cuda')

        def inner(arr):
            copy = torch.from_numpy(arr).to('cuda')
            return copy

        return inner

    def imports(self) -> Dict[str, Any]:
        """ Returns any imports required for the framework.
        :returns: A dictionary of imports.
        """
        import torch
        return {'torch': torch}

    def exec_str(self, bench: Benchmark, impl: Callable = None):
        """ Generates the execution-string that should be used to call
        the benchmark implementation.
        :param bench: A benchmark.
        :param impl: A benchmark implementation.
        """

        arg_str = self.arg_str(bench, impl)
        # param_str = self.param_str(bench, impl)
        main_exec_str = "__npb_result = __npb_impl({a})".format(a=arg_str)
        sync_str = "torch.cuda.synchronize()"
        return main_exec_str + "; " + sync_str
