import os

import torch

def go_fast(a: torch.Tensor) -> torch.Tensor:

    @torch.compile(mode='max-autotune')
    def body_fn(trace, diag):
        return trace + torch.tanh(diag)

    trace = torch.tensor([0.0], dtype=a.dtype, device=a.device)
    mark_step_begin = getattr(getattr(torch, "compiler", None), "cudagraph_mark_step_begin", None)
    for i in range(a.size(0)):
        # With torch.compile(mode="max-autotune") on CUDA, Inductor may use
        # CUDAGraphs and reuse a static output buffer across invocations.
        # If we carry the returned tensor into the next iteration, it can get
        # overwritten by the next run unless we mark step boundaries.
        mark_step_begin()
        trace = body_fn(trace, a[i, i])
    return a + trace


# # UNROLL IMPLEMENTATION:
# @torch.compile  # (mode="reduce-overhead")  # try reduce overhead
# def body_fn(a, trace, unroll):
#     for k in range(unroll):
#         trace = trace + torch.tanh(a[k, k])
#     return trace


# UNROLL_LIST = [int(os.environ.get("UNROLL", 100))]


# # @torch.compile(mode='reduce-overhead') # try reduce overhead
# def go_fast(a: torch.Tensor) -> torch.Tensor:
#     trace = torch.tensor(0, dtype=a.dtype, device=a.device)

#     i = 0
#     for unroll in UNROLL_LIST:
#         while i + unroll <= a.size(0):
#             trace = body_fn(a[i : i + unroll, i : i + unroll], trace, unroll)
#             i += unroll
#     # cleanup
#     while i < a.size(0):
#         trace = trace + torch.tanh(a[i, i])
#         i += 1

#     return a + trace
