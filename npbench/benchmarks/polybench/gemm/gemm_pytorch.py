import torch

def kernel(alpha, beta, C, A, B):
    return alpha * A @ B + beta * C