# Copyright 2021 ETH Zurich and the NPBench authors. All rights reserved.
import pathlib

try:
    import jax.numpy as jnp
    import jax

    jax.config.update("jax_enable_x64", True)
except ImportError:
    print(
        "WARNING: JAX is not installed. "
        "Please install JAX to run benchmarks with the JAX framework."
    )

from npbench.infrastructure import Benchmark, Framework
from typing import Any, Callable, Dict


_impl = {"lib-implementation": "lib"}


class JaxFramework(Framework):
    """A class for reading and processing framework information."""

    def __init__(self, fname: str):
        """Reads framework information.
        :param fname: The framework name.
        """

        super().__init__(fname)

        # Determine desired architecture from framework info and select device
        arch = self.info.get("arch", "cpu").lower()
        self._arch = arch
        # jax and jnp are imported at module level; ensure they exist
        try:
            self._jax = jax
            self._jnp = jnp
        except NameError:
            raise RuntimeError("JAX is not available in the current environment")

        # Choose device according to requested arch
        if arch == "gpu":
            gpu_devices = jax.devices("gpu")
            print("jax gpu devices:", gpu_devices, gpu_devices[0].device_kind)
            if not gpu_devices:
                raise RuntimeError("JAX GPU framework requested but no GPU device is available")
            self._device = gpu_devices[0]
        else:
            # default to CPU device
            cpu_devices = jax.devices("cpu")
            print("jax cpu devices:", cpu_devices)
            if not cpu_devices:
                raise RuntimeError("JAX CPU framework requested but no CPU device is available")
            self._device = cpu_devices[0]

    def imports(self) -> Dict[str, Any]:
        # expose jax, jnp and the selected device
        return {"jax": self._jax, "jnp": self._jnp, "device": self._device}

    def version(self):
        return self._jax.__version__

    def copy_func(self) -> Callable:
        """Returns the copy-method that should be used
        for copying the benchmark arguments."""
        jax = self._jax
        device = self._device

        def inner(arr):
            # Use device_put to place arrays on the chosen device
            try:
                return jax.device_put(arr, device)
            except Exception:
                # fallback to array conversion
                return self._jnp.array(arr)

        return inner

    def copy_back_func(self) -> Callable:
        """Transform device values back to host numpy arrays for validation."""
        jax = self._jax

        def inner(value):
            try:
                return jax.device_get(value)
            except Exception:
                # if it's already a numpy array or python scalar, return as-is
                return value

        return inner

    def impl_files(self, bench: Benchmark):
        """Returns the framework's implementation files for a particular
        benchmark.
        :param bench: A benchmark.
        :returns: A list of the benchmark implementation files.
        """

        parent_folder = pathlib.Path(__file__).parent.absolute()
        implementations = []

        # appending the default implementation
        pymod_path = parent_folder.joinpath(
            "..",
            "..",
            "npbench",
            "benchmarks",
            bench.info["relative_path"],
            bench.info["module_name"] + "_" + self.info["postfix"] + ".py",
        )

        implementations.append((pymod_path, "default"))

        for impl_name, impl_postfix in _impl.items():
            pymod_path = parent_folder.joinpath(
                "..",
                "..",
                "npbench",
                "benchmarks",
                bench.info["relative_path"],
                bench.info["module_name"]
                + "_"
                + self.info["postfix"]
                + "_"
                + impl_postfix
                + ".py",
            )
            implementations.append((pymod_path, impl_name))

        return implementations

    def implementations(self, bench: Benchmark):
        """Returns the framework's implementations for a particular benchmark.
        :param bench: A benchmark.
        :returns: A list of the benchmark implementations.
        """

        module_pypath = "npbench.benchmarks.{r}.{m}".format(
            r=bench.info["relative_path"].replace("/", "."), m=bench.info["module_name"]
        )
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
            implementations.append((ldict["impl"], "default"))
        except Exception as e:
            print(
                "Failed to load the {r} {f} implementation.".format(
                    r=self.info["full_name"], f=func_str
                )
            )
            raise e

        for impl_name, impl_postfix in _impl.items():
            ldict = dict()
            try:
                exec(
                    "from {m}_{p} import {f} as impl".format(
                        m=module_str, p=impl_postfix, f=func_str
                    ),
                    ldict,
                )
                implementations.append((ldict["impl"], impl_name))
            except ImportError:
                continue
            except Exception:
                print(
                    "Failed to load the {r} {f} implementation.".format(
                        r=self.info["full_name"], f=impl_name
                    )
                )
                continue

        return implementations

    def _autodiff(self, bench: Benchmark) -> Dict[str, Any]:
        return bench.info.get("autodiff", {})

    def setup_str(self, bench: Benchmark, impl: Callable = None, mode: str = "forward"):
        base = super().setup_str(bench, impl)
        if mode != "backward":
            return base

        ad = self._autodiff(bench)
        input_args = bench.info.get("input_args", [])
        grad_inputs = ad.get("grad_inputs", [])
        grad_indices = [
            input_args.index(arg) for arg in grad_inputs if arg in input_args
        ]
        arg_names = self.args(bench, impl)
        args_tuple = ", ".join(arg_names)
        if len(arg_names) == 1:
            args_tuple += ","

        target = ad.get("loss", {}).get("target", "result")
        if target == "result":
            loss_lines = [
                "    _out = __npb_impl(*args)",
                "    if isinstance(_out, tuple):",
                "        return jnp.sum(jnp.stack([jnp.sum(x) for x in _out]))",
                "    return jnp.sum(_out)",
            ]
        else:
            target_index = input_args.index(target)
            loss_lines = [f"    return jnp.sum(args[{target_index}])"]

        lines = []
        if base and base != "pass":
            lines.append(base)
        lines.append(f"__npb_args = ({args_tuple})")
        if grad_indices:
            grad_indices_str = ", ".join(str(idx) for idx in grad_indices)
            if len(grad_indices) == 1:
                grad_indices_str += ","
            lines.append(f"__npb_grad_indices = ({grad_indices_str})")
        else:
            lines.append("__npb_grad_indices = tuple()")
        lines.append("def __npb_loss_fn(*args):")
        lines.extend(loss_lines)
        lines.append("__npb_primal, __npb_vjp_full = jax.vjp(__npb_loss_fn, *__npb_args)")
        lines.append("__npb_cotangent = jnp.ones_like(__npb_primal)")
        lines.append("__npb_vjp = jax.jit(lambda ct: __npb_vjp_full(ct))")
        lines.append("__npb_vjp_warm = __npb_vjp(__npb_cotangent)")
        lines.append(
            "__npb_vjp_warm = (__npb_vjp_warm,) if not isinstance(__npb_vjp_warm, (tuple, list)) else tuple(__npb_vjp_warm)"
        )
        lines.append(
            "__npb_vjp_warm = tuple("
            "    jax.device_get(x if hasattr(x, 'block_until_ready') else x)"
            "    for x in jax.tree_util.tree_map("
            "        lambda x: x.block_until_ready() if hasattr(x, 'block_until_ready') else x,"
            "        __npb_vjp_warm"
            "    )"
            ")"
        )
        return "\n".join(lines) if lines else "pass"

    def exec_str(self, bench: Benchmark, impl: Callable = None, mode: str = "forward"):
        """Generates the execution-string that should be used to call
        the benchmark implementation.
        :param bench: A benchmark.
        :param impl: A benchmark implementation.
        """
        if mode == "backward":
            stmts = [
                "__npb_grads = __npb_vjp(__npb_cotangent)",
                "__npb_grads = (__npb_grads,) if not isinstance(__npb_grads, (tuple, list)) else tuple(__npb_grads)",
                "__npb_selected = tuple(__npb_grads[i] for i in __npb_grad_indices) if __npb_grad_indices else tuple()",
                # Block on device to mirror the sync we do for PyTorch CUDA, but keep grads on device
                "__npb_selected = tuple(g.block_until_ready() if hasattr(g, 'block_until_ready') else g for g in __npb_selected)",
                "__npb_result = __npb_selected",
            ]
            return "; ".join(stmts)

        arg_str = self.arg_str(bench, impl)
        main_exec_str = "__npb_result = jax.block_until_ready(__npb_impl({a}))".format(
            a=arg_str
        )
        return main_exec_str
