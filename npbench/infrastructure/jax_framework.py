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

    def imports(self) -> Dict[str, Any]:
        return {"jax": jax, "jnp": jnp}

    def copy_func(self) -> Callable:
        """Returns the copy-method that should be used
        for copying the benchmark arguments."""
        return jnp.array

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

    def exec_str(self, bench: Benchmark, impl: Callable = None, mode: str = "forward"):
        """Generates the execution-string that should be used to call
        the benchmark implementation.
        :param bench: A benchmark.
        :param impl: A benchmark implementation.
        """
        if mode == "backward":
            ad = self._autodiff(bench)
            input_args = bench.info.get("input_args", [])
            grad_inputs = ad.get("grad_inputs", [])
            grad_indices = [
                input_args.index(arg) for arg in grad_inputs if arg in input_args
            ]
            argnums_str = (
                "("
                + ", ".join(str(idx) for idx in grad_indices)
                + ("," if len(grad_indices) == 1 else "")
                + ")"
                if grad_indices
                else "()"
            )
            arg_names = self.args(bench, impl)
            args_tuple = ", ".join(arg_names)
            if len(arg_names) == 1:
                args_tuple += ","
            loss_target = ad.get("loss", {}).get("target", "result")
            if loss_target == "result":
                loss_expr = "(lambda r: jnp.sum(sum(r)) if isinstance(r, tuple) else jnp.sum(r))(__npb_impl(*args))"
            else:
                target_index = input_args.index(loss_target)
                loss_expr = f"jnp.sum(args[{target_index}])"
            stmts = [
                f"__npb_args = ({args_tuple})",
                f"__npb_loss_fn = lambda *args: {loss_expr}",
                f"__npb_loss, __npb_grads = jax.value_and_grad(__npb_loss_fn, argnums={argnums_str})(*__npb_args)",
                "__npb_grads = (__npb_grads,) if not isinstance(__npb_grads, (tuple, list)) else tuple(__npb_grads)",
                "__npb_loss = __npb_loss.block_until_ready()",
                "__npb_grads = tuple(g.block_until_ready() for g in __npb_grads)",
                "__npb_result = tuple(jax.device_get(g) for g in __npb_grads)",
            ]
            return "; ".join(stmts)

        arg_str = self.arg_str(bench, impl)
        main_exec_str = "__npb_result = jax.block_until_ready(__npb_impl({a}))".format(
            a=arg_str
        )
        return main_exec_str
