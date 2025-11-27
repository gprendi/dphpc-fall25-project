import torch


@torch.compile
def kernel(alpha, beta, A, B, x):
    return (alpha * A + beta * B) @ x
