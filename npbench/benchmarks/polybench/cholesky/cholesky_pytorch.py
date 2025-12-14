import torch

def _chol_panel(B: torch.Tensor) -> torch.Tensor:
    m = B.shape[0]
    rows = []
    for i in range(m):
        row = torch.zeros_like(B[i])
        for j in range(i):
            s = torch.dot(row[:j].clone(), rows[j][:j])
            row[j] = (B[i, j] - s) / rows[j][j]
        s = torch.dot(row[:i].clone(), row[:i].clone())
        row[i] = torch.sqrt(B[i, i] - s)
        rows.append(row)
    return torch.stack(rows, 0)

def kernel(A: torch.Tensor) -> torch.Tensor:
    n = A.shape[0]
    R = A.clone()
    L = torch.zeros_like(A)

    b = 4 # tune: 32/64 are usually good on CPU for n=100..500

    for k in range(0, n, b):
        bk = min(b, n - k)

        Akk = R[k:k+bk, k:k+bk].clone()
        Lkk = _chol_panel(Akk)
        L[k:k+bk, k:k+bk] = Lkk

        k2 = k + bk
        if k2 < n:
            Ak1 = R[k2:n, k:k+bk].clone()
            L21 = torch.linalg.solve_triangular(Lkk, Ak1.T, upper=False).T
            L[k2:n, k:k+bk] = L21

            R[k2:n, k2:n] = R[k2:n, k2:n] - L21 @ L21.T

    return torch.triu(A, 1) + torch.tril(L)
