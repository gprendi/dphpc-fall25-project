import torch


def kernel(alpha, A, B):
    strict_upper = torch.triu(A, diagonal=1)
    updated = B + torch.matmul(strict_upper, B)
    return updated * alpha
