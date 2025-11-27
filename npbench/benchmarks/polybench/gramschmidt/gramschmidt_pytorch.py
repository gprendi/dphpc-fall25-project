import torch


@torch.compile
def kernel(A, row, column):
    num_cols = A.shape[1]
    working_cols = [A[:, j] for j in range(num_cols)]
    q_columns = []
    r_rows = []

    for k in range(num_cols):
        a_k = working_cols[k]
        nrm = torch.dot(a_k, a_k)
        r_kk = torch.sqrt(nrm)
        q_k = a_k / r_kk
        q_columns.append(q_k)

        row_entries = []
        for j in range(num_cols):
            if j < k:
                zero_val = torch.zeros((), dtype=A.dtype, device=A.device)
                row_entries.append(zero_val)
                continue
            if j == k:
                row_entries.append(r_kk)
                continue

            a_j = working_cols[j]
            r_kj = torch.dot(q_k, a_j)
            working_cols[j] = a_j - q_k * r_kj
            row_entries.append(r_kj)

        r_rows.append(torch.stack(row_entries))

    Q = torch.stack(q_columns, dim=1)
    R = torch.stack(r_rows, dim=0)
    return Q, R
