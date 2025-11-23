import numpy as np


def kernel(A, x):

    y = (A @ x) @ A
    return y
