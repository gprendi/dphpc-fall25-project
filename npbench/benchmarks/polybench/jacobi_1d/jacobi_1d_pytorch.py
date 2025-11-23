import torch

# GPU: M dataset - without loop_body: 1988ms, clone in loop_body: 1014ms (JAX: 47ms)
# GPU: paper dataset - without loop_body: 2672ms, clone in loop_body: 1350ms (JAX: 72ms)

# CPU: M dataset - without loop_body: 1511ms, clone in loop_body: 994ms (JAX: 494ms)
# CPU: paper dataset - without loop_body: 3918ms, clone in loop_body: 1966ms (JAX: 1860ms)

def kernel(
    TSTEPS: int, A: torch.Tensor, B: torch.Tensor
):
    @torch.compile
    def loop_body(A, B):
        A = A.clone()
        B = B.clone() 
        B[1:-1] = 0.33333 * (A[:-2] + A[1:-1] + A[2:])
        A[1:-1] = 0.33333 * (B[:-2] + B[1:-1] + B[2:])
        return A, B

    for t in range(1, TSTEPS):
        A, B = loop_body(A, B)
    return A , B
