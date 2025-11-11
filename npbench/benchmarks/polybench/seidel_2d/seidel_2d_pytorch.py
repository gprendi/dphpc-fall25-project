import torch


def kernel(TSTEPS, N, A: torch.Tensor) -> torch.Tensor:

    A_res = A.clone() if A.requires_grad else A
    for t in range(0, TSTEPS - 1):
        for i in range(1, N - 1):
            A_res[i, 1:-1] += (A_res[i - 1, :-2] + A_res[i - 1, 1:-1] + A_res[i - 1, 2:] +
                           A_res[i, 2:] + A_res[i + 1, :-2] + A_res[i + 1, 1:-1] +
                           A_res[i + 1, 2:])
            for j in range(1, N - 1):
                A_res[i, j] += A_res[i, j - 1]
                A_res[i, j] /= 9.0

    return A_res