import torch

# Partially optimized

# def _chol_panel(B: torch.Tensor) -> torch.Tensor:
#     m = B.shape[0]
#     rows = []
#     for i in range(m):
#         row = torch.zeros_like(B[i])
#         for j in range(i):
#             s = torch.dot(row[:j].clone(), rows[j][:j])
#             row[j] = (B[i, j] - s) / rows[j][j]
#         s = torch.dot(row[:i].clone(), row[:i].clone())
#         row[i] = torch.sqrt(B[i, i] - s)
#         rows.append(row)
#     return torch.stack(rows, 0)

# def kernel(A: torch.Tensor) -> torch.Tensor:
#     n = A.shape[0]
#     R = A.clone()
#     L = torch.zeros_like(A)

#     b = 4 # tune: 32/64 are usually good on CPU for n=100..500

#     for k in range(0, n, b):
#         bk = min(b, n - k)

#         Akk = R[k:k+bk, k:k+bk].clone()
#         Lkk = _chol_panel(Akk)
#         L[k:k+bk, k:k+bk] = Lkk

#         k2 = k + bk
#         if k2 < n:
#             Ak1 = R[k2:n, k:k+bk].clone()
#             L21 = torch.linalg.solve_triangular(Lkk, Ak1.T, upper=False).T
#             L[k2:n, k:k+bk] = L21

#             R[k2:n, k2:n] = R[k2:n, k2:n] - L21 @ L21.T

#     return torch.triu(A, 1) + torch.tril(L)








def kernel(A):

    @torch.compile
    def _set(M, i, j, v):
        N = M.clone()
        N[i, j] = v
        return N
    
    n = A.shape[0]
    W = A.clone()
    W = _set(W, 0, 0, torch.sqrt(torch.clamp(W[0, 0], min=0.0)))
    ar = torch.arange(n, device=A.device)
    zrow = torch.zeros(n, dtype=A.dtype, device=A.device)

    for i in range(1, n):
        for j in range(n):
            if j < i:
                m = ar < j
                ai = torch.where(m, W[i, :], zrow)
                aj = torch.where(m, W[j, :], zrow)
                W = _set(W, i, j, (W[i, j] - torch.dot(ai, aj)) / W[j, j])
        m = ar < i
        ai = torch.where(m, W[i, :], zrow)
        W = _set(W, i, i, torch.sqrt(torch.clamp(W[i, i] - torch.dot(ai, ai), min=0.0)))
    return W