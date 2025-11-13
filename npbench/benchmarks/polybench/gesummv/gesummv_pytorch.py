import torch


def kernel(alpha, beta, A, B, x):
    return torch.matmul(alpha * A + beta * B, x)
