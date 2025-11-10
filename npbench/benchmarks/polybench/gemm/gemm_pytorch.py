import torch

@torch.compile
def kernel(alpha, beta, C, A, B):
    return alpha * A @ B + beta * C