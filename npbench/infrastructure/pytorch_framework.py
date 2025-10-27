from npbench.infrastructure import Benchmark, Framework
from typing import Any, Callable, Dict
import pathlib

_impl = {}


class PytorchFramework(Framework):
    """A framework adapter that routes NPBench benchmarks through PyTorch."""

    def __init__(self, fname: str):
        """Initialise PyTorch framework metadata and target device."""
        super().__init__(fname)
        try:
            import torch
        except ImportError as exc:
            raise RuntimeError("PyTorch is not installed, cannot initialise PyTorch framework.") from exc

        arch = self.info.get("arch", "cpu").lower()
        if arch == "gpu":
            if not torch.cuda.is_available():
                raise RuntimeError("PyTorch GPU framework requested but CUDA is not available.")
            self._device = torch.device("cuda")
            self._needs_sync = True
        else:
            self._device = torch.device("cpu")
            self._needs_sync = False

        self._torch = torch
        self._arch = arch

    def version(self) -> str:
        return self._torch.__version__

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
        """Return a copier that materialises tensors on the configured device."""
        torch = self._torch
        device = self._device

        def inner(arr):
            if isinstance(arr, torch.Tensor):
                tensor = arr.to(device=device).detach()
                return tensor.clone()
            return torch.tensor(arr, device=device)

        return inner

    def copy_back_func(self) -> Callable:
        """Transform tensors back to host numpy arrays for validation."""
        torch = self._torch

        def inner(value):
            if isinstance(value, torch.Tensor):
                return value.detach().cpu().numpy()
            return value

        return inner

    def imports(self) -> Dict[str, Any]:
        """ Returns any imports required for the framework.
        :returns: A dictionary of imports.
        """
        return {'torch': self._torch}

    def _prefixed(self, bench: Benchmark, arg: str) -> str:
        if arg in bench.info.get("array_args", []):
            return f"__npb_{self.info['prefix']}_{arg}"
        return arg

    def _autodiff(self, bench: Benchmark) -> Dict[str, Any]:
        return bench.info.get("autodiff", {})

    def setup_str(self, bench: Benchmark, impl: Callable = None, mode: str = "forward") -> str:
        base = super().setup_str(bench, impl)
        extra = []
        if mode == "backward":
            ad = self._autodiff(bench)
            grad_inputs = ad.get("grad_inputs", [])
            for arg in grad_inputs:
                if arg not in bench.info.get("array_args", []):
                    continue
                pref = self._prefixed(bench, arg)
                extra.append(f"{pref}.requires_grad_(True)")
                extra.append(f"({pref}.grad.zero_() if {pref}.grad is not None else None)")
        parts = []
        if base and base != "pass":
            parts.append(base)
        parts.extend(extra)
        stmt = "; ".join(parts) if parts else "pass"
        if self._needs_sync:
            sync = "torch.cuda.synchronize()"
            return sync if stmt == "pass" else f"{stmt}; {sync}"
        return stmt

    def exec_str(self, bench: Benchmark, impl: Callable = None, mode: str = "forward"):
        """ Generates the execution-string that should be used to call
        the benchmark implementation.
        :param bench: A benchmark.
        :param impl: A benchmark implementation.
        """
        arg_str = self.arg_str(bench, impl)
        if mode == "backward":
            ad = self._autodiff(bench)
            grad_inputs = ad.get("grad_inputs", [])
            target = ad.get("loss", {}).get("target", "result")

            call_stmt = "__npb_forward = __npb_impl({a})".format(a=arg_str)
            if target == "result":
                loss_expr = "__npb_forward.sum()"
            else:
                loss_expr = f"{self._prefixed(bench, target)}.sum()"
            loss_stmt = "__npb_loss = {expr}".format(expr=loss_expr)
            backward_stmt = "__npb_loss.backward()"
            grad_exprs = []
            for arg in grad_inputs:
                if arg not in bench.info.get("array_args", []):
                    continue
                pref = self._prefixed(bench, arg)
                grad_exprs.append(f"({pref}.grad.detach().clone() if {pref}.grad is not None else None)")
            grads_stmt = "__npb_result = ({})".format(", ".join(grad_exprs)) if grad_exprs else "__npb_grads = tuple()"
            #result_stmt = "__npb_result = (__npb_loss.detach(),) + tuple(__npb_grads)"
            stmts = [call_stmt, loss_stmt, backward_stmt, grads_stmt]
            if self._needs_sync:
                stmts.append("torch.cuda.synchronize()")
            return "; ".join(stmts)

        main_exec_str = "__npb_result = __npb_impl({a})".format(a=arg_str)
        if self._needs_sync:
            sync_str = "torch.cuda.synchronize()"
            return main_exec_str + "; " + sync_str
        return main_exec_str
