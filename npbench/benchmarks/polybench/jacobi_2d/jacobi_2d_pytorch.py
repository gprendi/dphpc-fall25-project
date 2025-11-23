import torch

# GPU: M dataset - without loop_body: 107ms, clone in loop_body: 36ms (JAX: 7ms)
# GPU: paper dataset - without loop_body: 22009ms, clone in loop_body: 3676ms (JAX: 2393ms)

def kernel(
    TSTEPS: int, A: torch.Tensor, B: torch.Tensor
):
    @torch.compile
    def loop_body(A, B):
        A = A.clone()
        B = B.clone() 
        B[1:-1, 1:-1] = 0.2 * (A[1:-1, 1:-1] + A[1:-1, :-2] + A[1:-1, 2:] +
                               A[2:, 1:-1] + A[:-2, 1:-1])
        A[1:-1, 1:-1] = 0.2 * (B[1:-1, 1:-1] + B[1:-1, :-2] + B[1:-1, 2:] +
                               B[2:, 1:-1] + B[:-2, 1:-1])
        return A, B

    for t in range(1, TSTEPS):
        A, B = loop_body(A, B)
    return A , B

# def kernel(
#     TSTEPS: int, A: torch.Tensor, B: torch.Tensor
# ):
#     A, B = (A.clone(), B.clone()) if A.requires_grad else (A, B)
#     for t in range(1, TSTEPS):
#         B[1:-1, 1:-1] = 0.2 * (A[1:-1, 1:-1] + A[1:-1, :-2] + A[1:-1, 2:] +
#                                A[2:, 1:-1] + A[:-2, 1:-1])
#         A[1:-1, 1:-1] = 0.2 * (B[1:-1, 1:-1] + B[1:-1, :-2] + B[1:-1, 2:] +
#                                B[2:, 1:-1] + B[:-2, 1:-1])

#     return A, B