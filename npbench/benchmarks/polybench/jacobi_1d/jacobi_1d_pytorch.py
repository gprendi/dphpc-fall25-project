import torch
from typing import Tuple


def kernel(
    TSTEPS: int, A: torch.Tensor, B: torch.Tensor
):
    A_res, B_res = (A.clone(), B.clone()) if A.requires_grad else (A, B)
    for t in range(1, TSTEPS):
        B_res[1:-1] = 0.33333 * (A_res[:-2] + A_res[1:-1] + A_res[2:])
        A_res[1:-1] = 0.33333 * (B_res[:-2] + B_res[1:-1] + B_res[2:])
    return torch.stack((A_res , B_res))
