import torch
import torch.nn.functional as F

def kernel(A):
    n = A.shape[0]
    indices = torch.arange(n)

    @torch.compile
    def update_single(A, i, j, indices):
        mask = (indices < j)
        dot = (A[i] * mask) @ (A[:, j] * mask)
        new_val = (A[i, j] - dot) / A[j, j]
        row_mask = F.one_hot(i, n)
        col_mask = F.one_hot(j, n)
        elem_mask = row_mask.unsqueeze(1) * col_mask.unsqueeze(0)
        return A + elem_mask * (new_val - A[i, j])

    @torch.compile
    def update_row_batch(A, i, indices):
        row_mask = (indices < i)
        col_mask = (indices >= i)
        left = A[i] * row_mask
        right = A * row_mask.unsqueeze(1)
        dots = left @ right
        delta = -dots * col_mask
        row_select = F.one_hot(i, n)
        return A + row_select.unsqueeze(1) * delta.unsqueeze(0)


    for i in range(n):
        i_t = torch.tensor(i)
        for j in range(i):
            j_t = torch.tensor(j)
            A = update_single(A, i_t, j_t, indices)
        A = update_row_batch(A, i_t, indices)

    return A
