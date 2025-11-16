import torch


@torch.compile
def kernel(A, x):
    tmp = torch.matmul(A, x)
    return torch.matmul(tmp, A)
