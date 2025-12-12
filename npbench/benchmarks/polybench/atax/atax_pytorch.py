import torch


@torch.compile
def kernel(A, x):
    y = (A @ x) @ A
    return y
