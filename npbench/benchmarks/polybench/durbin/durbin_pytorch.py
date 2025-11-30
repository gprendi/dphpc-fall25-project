import torch
torch.autograd.set_detect_anomaly(True)

def kernel(r):

    y = torch.empty_like(r)
    alpha = -r[0]
    beta = torch.tensor([1.0], dtype=r.dtype, device=r.device)
    y[0] = -r[0]

    for k in range(1, r.shape[0]):
        beta = beta.clone()
        beta *= 1.0 - alpha * alpha
        alpha = -(r[k] + torch.dot(torch.flip(r[:k], [0]), y[:k])) / beta
        y = y.clone()
        y[:k] += alpha * torch.flip(y[:k], [0])
        y[k] = alpha

    return y
