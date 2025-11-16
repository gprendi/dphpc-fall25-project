import torch


@torch.compile
def kernel(alpha, beta, A, B, C, D):
    tmp = torch.matmul(A, B)
    result = alpha * torch.matmul(tmp, C) + beta * D
    if D.requires_grad:
        return result
    D.copy_(result)
    return D
