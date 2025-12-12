import torch


@torch.compile
def kernel(alpha, beta, A, u1, v1, u2, v2, w, x, y, z):
    updated_A = A + torch.outer(u1, v1) + torch.outer(u2, v2)
    updated_x = x + beta * y @ updated_A + z
    updated_w = w + alpha * updated_A @ updated_x
    return updated_A, updated_w, updated_x
