# Copyright 2021 ETH Zurich and the NPBench authors. All rights reserved.
import time
from pathlib import Path

from npbench.infrastructure import (Benchmark,generate_framework, Framework, timeout_decorator as tout, utilities as util)
from typing import Any, Callable, Dict, Sequence, Tuple
from torchviz import make_dot


class Test(object):
    """ A class for testing a framework on a benchmark. """

    def __init__(self, bench: Benchmark, frmwrk: Framework, npfrmwrk: Framework = None, jaxfrmwrk: Framework = None, visualize = False):
        self.bench = bench
        self.frmwrk = frmwrk
        self.numpy = npfrmwrk
        self.jax = jaxfrmwrk
        self.visualize = visualize
        self._captured_exec_state = None

    def _execute(self, frmwrk: Framework, impl: Callable, impl_name: str, mode: str, bdata: Dict[str, Any], repeat: int,
                 ignore_errors: bool, exec_mode: str = "forward", capture_state: bool = False, warmup: int = 3) -> Tuple[Any, Sequence[float]]:
        report_str = frmwrk.info["full_name"] + " - " + impl_name
        try:
            copy = frmwrk.copy_func()
            setup_str = frmwrk.setup_str(self.bench, impl, mode=exec_mode)
            exec_str = frmwrk.exec_str(self.bench, impl, mode=exec_mode)
        except Exception as e:
            print("Failed to load the {} implementation.".format(report_str))
            print(e)
            if not ignore_errors:
                raise
            return None, None
        ldict = {'__npb_impl': impl, '__npb_copy': copy, **bdata}
        try:
            out, timelist = util.benchmark(exec_str, setup_str, report_str + " - " + mode, repeat, ldict,
                                           '__npb_result', warmup=warmup)
        except Exception as e:
            print("Failed to execute the {} implementation.".format(report_str))
            print(e)
            if not ignore_errors:
                raise
            return None, None

        if out is not None:
            if isinstance(out, (tuple, list)):
                out = list(out)
            else:
                out = [out]
        else:
            out = []
        if "output_args" in self.bench.info.keys() and exec_mode == "forward":
            num_output_args = len(self.bench.info["output_args"])
            # out += [ldict[a] for a in frmwrk.inout_args(self.bench)]
            # print("Number of output arguments:", num_output_args, " vs ", len(out))
            # print("Output arguments:", self.bench.info["output_args"], " vs ", out)
            assert len(out) == num_output_args, str("Number of output arguments does not match.", "Number of output arguments:", num_output_args, " vs ", len(out))
        elif "autodiff" in self.bench.info.keys() and exec_mode == "backward":
            num_input_args = len(self.bench.info["autodiff"].get("grad_inputs", []))
            # out += [ldict[a] for a in frmwrk.inout_args(self.bench)]
            # print("Number of input arguments:", num_input_args, " vs ", len(out))
            # print("Output grads :", self.bench.info["output_args"], " vs ", out)
            assert len(out) == num_input_args, str("Number of output grads arguments does not match.", "Number of input arguments:", num_input_args, " vs ", len(out))

        # save locals dictionary from the execution if we're gonna visualize
        if capture_state:
            self._captured_exec_state = dict(ldict)
        else:
            self._captured_exec_state = None

        return out, timelist

    def run(self, preset: str, validate: bool, repeat: int, timeout: float = 200.0, ignore_errors: bool = False,
            mode: str = "forward", warmup: int = 3):
        """ Tests the framework against the benchmark.
        :param preset: The preset to use for testing (S, M, L, paper).
        :param validate: If true, it validates the output against NumPy.
        :param repeat: The number of repeatitions.
        :param warmup: Number of warm-up executions before timing.
        """
        print("***** Testing {f} with {b} on the {p} dataset *****".format(b=self.bench.bname,
                                                                           f=self.frmwrk.info["full_name"],
                                                                           p=preset))
        exec_mode = mode if mode in ("forward", "backward") else "forward"
        do_validate = validate
        bdata = self.bench.get_data(preset)
        params = self.bench.info.get("parameters", {})
        viz_preset = "visualize" if "visualize" in params else None

        # Run NumPy for validation
        if do_validate and self.frmwrk.fname != "numpy" and self.numpy and mode == "forward":
            np_impl, np_impl_name = self.numpy.implementations(self.bench)[0]
            np_out, _ = self._execute(self.numpy, np_impl, np_impl_name, "validation", bdata, 1, ignore_errors,
                                      exec_mode="forward")
            jax_out = None
        elif do_validate and mode != "forward" and self.jax:
            jax_context = {**bdata, **self.jax.imports()}
            jax_impl, jax_impl_name = self.jax.implementations(self.bench)[0]
            jax_out, _ = self._execute(self.jax, jax_impl, jax_impl_name, "validation", jax_context, 1, ignore_errors,
                                      exec_mode="backward")
            np_out = None
        else:
            do_validate = False
            np_out = None
            jax_out = None

        # Extra information
        kind = ""
        if "kind" in self.bench.info.keys():
            kind = self.bench.info["kind"]
        domain = ""
        if "domain" in self.bench.info.keys():
            domain = self.bench.info["domain"]
        dwarf = ""
        if "dwarf" in self.bench.info.keys():
            dwarf = self.bench.info["dwarf"]
        version = self.frmwrk.version()

        @tout.exit_after(timeout)
        def first_execution(impl, impl_name):
            return self._execute(self.frmwrk, impl, impl_name, f"first/{exec_mode}", context, 1, ignore_errors,
                                 exec_mode=exec_mode)

        bvalues = []
        context = {**bdata, **self.frmwrk.imports()}
        for impl, impl_name in self.frmwrk.implementations(self.bench):
            # First execution
            try:
                frmwrk_out, _ = first_execution(impl, impl_name)
            except KeyboardInterrupt:
                print("Implementation \"{}\" timed out.".format(impl_name), flush=True)
                continue
            except Exception:
                if not ignore_errors:
                    raise
                continue

            # Validation
            valid = True
            if do_validate and np_out is not None and mode == 'forward':
                try:
                    if isinstance(frmwrk_out, (tuple, list)):
                        frmwrk_out = [self.frmwrk.copy_back_func()(a) for a in frmwrk_out]
                    else:
                        frmwrk_out = self.frmwrk.copy_back_func()(frmwrk_out)

                    frmwrk_name = self.frmwrk.info["full_name"] + " - " + impl_name


                    rtol = 1e-5 if not 'rtol' in self.bench.info else self.bench.info['rtol']
                    atol = 1e-8 if not 'atol' in self.bench.info else self.bench.info['atol']
                    norm_error = 1e-5 if not 'norm_error' in self.bench.info else self.bench.info['norm_error']
                    valid = util.validate(np_out, frmwrk_out, frmwrk_name, rtol=rtol, atol=atol, norm_error=norm_error)
                    if valid:
                        print("{} - {} - validation: SUCCESS".format(frmwrk_name, impl_name))
                    elif not ignore_errors:
                        raise ValueError("{} did not validate!".format(frmwrk_name))
                except Exception:
                    print("Failed to run {} validation.".format(self.frmwrk.info["full_name"]))
                    if not ignore_errors:
                        raise
            elif do_validate and jax_out is not None and mode != "forward":
                try:
                    if isinstance(frmwrk_out, (tuple, list)):
                        frmwrk_out = [self.frmwrk.copy_back_func()(a) for a in frmwrk_out]
                    else:
                        frmwrk_out = self.frmwrk.copy_back_func()(frmwrk_out)

                    frmwrk_name = self.frmwrk.info["full_name"] + " - " + impl_name


                    rtol = 1e-5 if not 'rtol' in self.bench.info else self.bench.info['rtol']
                    atol = 1e-8 if not 'atol' in self.bench.info else self.bench.info['atol']
                    norm_error = 1e-5 if not 'norm_error' in self.bench.info else self.bench.info['norm_error']
                    valid = util.validate(jax_out, frmwrk_out, frmwrk_name, rtol=rtol, atol=atol, norm_error=norm_error)
                    if valid:
                        print("{} - {} - validation: SUCCESS".format(frmwrk_name, impl_name))
                    elif not ignore_errors:
                        raise ValueError("{} did not validate!".format(frmwrk_name))
                except Exception:
                    print("Failed to run {} validation.".format(self.frmwrk.info["full_name"]))
                    if not ignore_errors:
                        raise

            # Capture visualization
            capture_viz = self.visualize and self.frmwrk.info["simple_name"].startswith("pytorch") and exec_mode == "backward"
            if capture_viz:
                viz_bdata = self.bench.get_data(viz_preset) if viz_preset else bdata
                viz_context = {**viz_bdata, **self.frmwrk.imports()}
                try:
                    # execute and save locals
                    self._execute(self.frmwrk, impl, impl_name, f"visualize/{exec_mode}", viz_context, 1, ignore_errors,
                                  exec_mode=exec_mode, capture_state=True)
                    # visualize execution
                    self._generate_visualization(impl_name, exec_mode)
                except Exception as exc:
                    msg = str(exc)
                    print(f"Failed to generate visualization for {impl_name}: {msg}")
                    if "make sure the Graphviz executables" in msg.lower():
                        print("You need to install graphviz (eg `brew install graphviz`).")

            # Main execution
            _, timelist = self._execute(self.frmwrk, impl, impl_name, f"median/{exec_mode}", context, repeat,
                                        ignore_errors, exec_mode=exec_mode, warmup=warmup)
            if timelist:
                for t in timelist:
                    name = impl_name if exec_mode == "forward" else f"{impl_name}:{exec_mode}"
                    bvalues.append(dict(details=name, validated=valid, time=t, mode=exec_mode))

        # create a database connection
        database = r"npbench.db"
        conn = util.create_connection(database)

        # create tables
        if conn is not None:
            # create results table
            util.create_table(conn, util.sql_create_results_table)
        else:
            print("Error! cannot create the database connection.")

        # Write data
        timestamp = int(time.time())
        for d in bvalues:
            new_d = {
                'timestamp': timestamp,
                'benchmark': self.bench.info["short_name"],
                'kind': kind,
                'domain': domain,
                'dwarf': dwarf,
                'preset': preset,
                'mode': d.get("mode", exec_mode),
                'framework': self.frmwrk.info["simple_name"],
                'version': version,
                'details': d["details"],
                'validated': d["validated"],
                'time': d["time"]
            }
            result = tuple(new_d.values())
            # print(result)
            util.create_result(conn, util.sql_insert_into_results_table, result)

    def _generate_visualization(self, impl_name: str, exec_mode: str) -> None:
        context = self._captured_exec_state
        if not context:
            return
        loss_tensor = context.get("__npb_loss") or context.get("__npb_forward")
        if isinstance(loss_tensor, (list, tuple)):
            loss_tensor = sum(loss_tensor)
        if loss_tensor is None or not hasattr(loss_tensor, "grad_fn"):
            return
        autodiff = self.bench.info.get("autodiff", {})
        grad_inputs = autodiff.get("grad_inputs", [])
        params = {}
        prefix = self.frmwrk.info.get("prefix", "")
        for arg in grad_inputs:
            key = f"__npb_{prefix}_{arg}"
            tensor = context.get(key)
            if tensor is not None and getattr(tensor, "requires_grad", False):
                params[arg] = tensor
        dot = make_dot(loss_tensor, params=params or None)
        out_dir = Path("visualizations")
        out_dir.mkdir(parents=True, exist_ok=True)
        stem = f"{self.bench.bname}_{self.frmwrk.info['simple_name']}_{impl_name}_{exec_mode}"
        output_path = out_dir / stem
        dot.render(str(output_path), format="pdf", cleanup=True)
        print(f"Saved visualization to {output_path.with_suffix('.pdf')}")
        self._captured_exec_state = None
