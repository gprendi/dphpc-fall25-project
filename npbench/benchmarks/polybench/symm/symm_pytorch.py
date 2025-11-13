import torch


def kernel(alpha, beta, C, A, B):
    C_res = C * beta
    m, n = C_res.shape
    for i in range(m):
        if i > 0:
            a_prefix = A[i, :i]
            C_res[:i, :] = C_res[:i, :] + alpha * torch.outer(a_prefix, B[i, :])
            temp2 = torch.matmul(B[:i, :].transpose(0, 1), a_prefix)
        else:
            temp2 = torch.zeros(n, dtype=C_res.dtype, device=C_res.device)
        C_res[i, :] = C_res[i, :] + alpha * B[i, :] * A[i, i] + alpha * temp2
    return C_res
