import numpy as np


def kernel(A, row, column):

    Q = np.zeros_like(A)
    R = np.zeros((column, column), dtype=A.dtype)

    for k in range(column):
        nrm = np.dot(A[:, k], A[:, k])
        R[k, k] = np.sqrt(nrm)
        Q[:, k] = A[:, k] / R[k, k]
        for j in range(k + 1, column):
            R[k, j] = np.dot(Q[:, k], A[:, j])
            A[:, j] -= Q[:, k] * R[k, j]

    return Q, R
