import torch


def kernel(alpha, beta, C, A, B):
    alpha_t = torch.as_tensor(alpha, dtype=C.dtype, device=C.device)
    beta_t = torch.as_tensor(beta, dtype=C.dtype, device=C.device)

    lower = beta_t * torch.tril(C)
    mixed = torch.matmul(A, B.transpose(-2, -1)) + torch.matmul(B, A.transpose(-2, -1))
    lower = lower + alpha_t * torch.tril(mixed)
    upper = torch.triu(C, diagonal=1)
    return lower + upper
