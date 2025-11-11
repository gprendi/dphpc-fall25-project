import torch
from typing import Tuple


def kernel(TSTEPS: int, A: torch.Tensor, B: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
    for t in range(1, TSTEPS):
        B[1:-1] = 0.33333 * (A[:-2] + A[1:-1] + A[2:])
        A[1:-1] = 0.33333 * (B[:-2] + B[1:-1] + B[2:])
    return A, B
