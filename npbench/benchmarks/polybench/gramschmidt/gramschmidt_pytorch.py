import torch
torch.autograd.set_detect_anomaly(True)
# @torch.compile
# def inner_1(A_view, Q_view):
#     nrm = torch.dot(A_view, A_view)
#     r_new = torch.sqrt(nrm)
#     Q_view.copy_(A_view / r_new)
#     return r_new

# @torch.compile
# def inner_2(A_view, Q_view):
#     r_new = torch.dot(Q_view, A_view)
#     A_view -= Q_view * r_new
#     return r_new

# def kernel(A, row, column):
#     Q = torch.zeros_like(A)
#     R = torch.zeros((A.shape[1], A.shape[1]), dtype=A.dtype, device=A.device)

#     for k in range(A.shape[1]):
#         A_view = A[:, k]
#         Q_view = Q[:, k]
#         R[k, k] = inner_1(A_view, Q_view)
#         for j in range(k + 1, A.shape[1]):
#             A_view = A[:, j]
#             R[k, j] = inner_2(A_view, Q_view)

#     return Q, R

# remove in-place operations
def kernel(A, row, column):
    A = A.clone()
    Q = torch.zeros_like(A)
    R = torch.zeros((A.shape[1], A.shape[1]), dtype=A.dtype, device=A.device)

    for k in range(A.shape[1]):
        nrm = torch.dot(A[:, k], A[:, k])
        R[k, k] = torch.sqrt(nrm)
        Q[:, k] = A[:, k] / R[k, k]
        for j in range(k + 1, A.shape[1]):
            R[k, j] = torch.dot(Q[:, k], A[:, j])
            A[:, j] = A[:, j] - Q[:, k] * R[k, j]

    return Q, R

# def kernel(A, row, column):
#     A = A.clone()
#     Q = torch.zeros_like(A)
#     R = torch.zeros((A.shape[1], A.shape[1]), dtype=A.dtype, device=A.device)

#     for k in range(A.shape[1]):
#         nrm = torch.dot(A[:, k], A[:, k])
#         R[k, k] = torch.sqrt(nrm)
#         Q[:, k] = A[:, k] / R[k, k]
#         for j in range(k + 1, A.shape[1]):
#             R[k, j] = torch.dot(Q[:, k], A[:, j])
#             A[:, j] -= Q[:, k] * R[k, j]

#     return Q, R
