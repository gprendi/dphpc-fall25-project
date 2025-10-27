import torch


def kernel(A):
    return torch.linalg.cholesky(A) + torch.triu(A, diagonal=1)