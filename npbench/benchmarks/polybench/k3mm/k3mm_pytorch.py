import torch


@torch.compile
def kernel(A, B, C, D):

    return A @ B @ C @ D