import os

import torch

# @torch.compile
# def body_fn(trace, diag):
#     return trace + torch.tanh(diag)

# def go_fast(a: torch.Tensor) -> torch.Tensor:

#     trace = torch.tensor([0.0], dtype=a.dtype, device=a.device)
#     for i in range(a.size(0)):
#         trace = body_fn(trace, a[i, i])
    
#     return a + trace


# UNROLL IMPLEMENTATION:
# @torch.compile  # (mode="reduce-overhead")  # try reduce overhead
def body_fn(a, trace, unroll):
    for k in range(unroll):
        trace = trace + torch.tanh(a[k, k])
    return trace


UNROLL_LIST = [int(os.environ.get("UNROLL", 1))]


# @torch.compile(mode='reduce-overhead') # try reduce overhead
def go_fast(a: torch.Tensor) -> torch.Tensor:
    trace = torch.tensor(0, dtype=a.dtype, device=a.device)

    i = 0
    for unroll in UNROLL_LIST:
        while i + unroll <= a.size(0):
            trace = body_fn(a[i : i + unroll, i : i + unroll], trace, unroll)
            i += unroll
    # cleanup
    while i < a.size(0):
        trace = trace + torch.tanh(a[i, i])
        i += 1

    return a + trace
