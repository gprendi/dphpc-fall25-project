import torch

# M dataset - clone in kernel: 28ms, clone in func_body: 20ms
# paper dataset - clone in kernel: 514ms, clone in func_body: 360ms

@torch.compile
def func_body(A, B):
    A = A.clone()
    B = B.clone()
    B[1:-1, 1:-1, 1:-1] = (
        0.125 * (A[2:, 1:-1, 1:-1] - 2.0 * A[1:-1, 1:-1, 1:-1] + A[:-2, 1:-1, 1:-1])
        + 0.125
        * (A[1:-1, 2:, 1:-1] - 2.0 * A[1:-1, 1:-1, 1:-1] + A[1:-1, :-2, 1:-1])
        + 0.125
        * (A[1:-1, 1:-1, 2:] - 2.0 * A[1:-1, 1:-1, 1:-1] + A[1:-1, 1:-1, 0:-2])
        + A[1:-1, 1:-1, 1:-1]
    )
    A[1:-1, 1:-1, 1:-1] = (
        0.125 * (B[2:, 1:-1, 1:-1] - 2.0 * B[1:-1, 1:-1, 1:-1] + B[:-2, 1:-1, 1:-1])
        + 0.125
        * (B[1:-1, 2:, 1:-1] - 2.0 * B[1:-1, 1:-1, 1:-1] + B[1:-1, :-2, 1:-1])
        + 0.125
        * (B[1:-1, 1:-1, 2:] - 2.0 * B[1:-1, 1:-1, 1:-1] + B[1:-1, 1:-1, 0:-2])
        + B[1:-1, 1:-1, 1:-1]
    )
    return A, B


def kernel(TSTEPS, A, B):
    # if A.requires_grad:
    #     A = A.clone()
    # if B.requires_grad:
    #     B = B.clone()

    for t in range(1, TSTEPS):
        A, B = func_body(A, B)
    return A, B
