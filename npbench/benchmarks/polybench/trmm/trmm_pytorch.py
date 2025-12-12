import torch


@torch.compile
def kernel(alpha, A, B):
    strict_upper = torch.triu(A, diagonal=1)
    updated_B1 = B + strict_upper @ B
    updated_B2 = updated_B1 * alpha

    return updated_B2
