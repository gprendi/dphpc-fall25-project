import torch


def kernel(A, x):
    tmp = torch.matmul(A, x)
    return torch.matmul(tmp, A)
