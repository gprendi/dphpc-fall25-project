import torch


def kernel(alpha, beta, C, A):
    alpha_t = torch.as_tensor(alpha, dtype=C.dtype, device=C.device)
    beta_t = torch.as_tensor(beta, dtype=C.dtype, device=C.device)

    lower = beta_t * torch.tril(C)
    gram = torch.matmul(A, A.transpose(-2, -1))
    lower = lower + alpha_t * torch.tril(gram)
    upper = torch.triu(C, diagonal=1)
    return lower + upper
