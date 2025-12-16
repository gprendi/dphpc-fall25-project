import torch


def kernel(M, data):
    # Clone to avoid in-place writes on a leaf that requires grad
    result = data.clone()
    for i in range(M):
        result[i] = 1.0
    return result
