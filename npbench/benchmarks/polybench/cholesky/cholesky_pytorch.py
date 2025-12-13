import torch


@torch.compile
def kernel(A):

    A = A.clone()
    A[0, 0] = torch.sqrt(A[0, 0])

    def row_update(i, A):

        def col_update(j, A):
            mask = torch.arange(A.shape[1], device=A.device) < j  # bool mask

            A_i_slice = torch.where(mask, A[i, :], torch.zeros_like(A[i, :]))
            A_j_slice = torch.where(mask, A[j, :], torch.zeros_like(A[j, :]))

            dot_product = torch.dot(A_i_slice, A_j_slice)
            A[i, j] = (A[i, j] - dot_product) / A[j, j]
            return A
        
        for j in range(0, i):
            A = col_update(j, A)

        A_i_slice = torch.where(
            torch.arange(A.shape[1], device=A.device) < i,
            A[i, :],
            torch.zeros_like(A[i, :]),
        )
        dot_product = torch.dot(A_i_slice, A_i_slice)
        A[i, i] = torch.sqrt(A[i, i] - dot_product)
        return A

    for i in range(1, A.shape[0]):
        A = row_update(i, A)

    return A
