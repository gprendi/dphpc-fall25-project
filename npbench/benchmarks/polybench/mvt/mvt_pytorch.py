import torch


@torch.compile
def kernel(x1, x2, y_1, y_2, A):

    updated_x1 = x1 + A @ y_1
    updated_x2 = x2 + y_2 @ A

    return updated_x1, updated_x2
