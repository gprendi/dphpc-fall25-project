import torch


@torch.compile
def kernel(A, x):
    tmp = torch.matmul(A, x)
    y = torch.matmul(tmp, A)
    return y
