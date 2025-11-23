import torch


@torch.compile
def kernel(alpha, beta, A, B, C, D):
    tmp = torch.matmul(A, B)
    D = alpha * torch.matmul(tmp, C) + beta * D
    return D
