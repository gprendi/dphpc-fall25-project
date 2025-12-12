import torch


@torch.compile
def kernel(alpha, beta, A, B, C, D):
    D = alpha * A @ B @ C + beta * D
    return D
