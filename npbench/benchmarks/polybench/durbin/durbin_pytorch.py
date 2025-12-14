import torch
torch.autograd.set_detect_anomaly(True)
import torch._functorch.config as config

config.donated_buffer=False
def kernel(r):

    y = torch.zeros_like(r)
    alpha = -r[0].clone()
    beta = torch.tensor([1.0], dtype=r.dtype, device=r.device)
    y[0] = -r[0]

    @torch.compile
    def loop_body(k, loop_vars):
        alpha, beta, y, r = loop_vars
        beta = beta.clone()
        beta *= 1.0 - alpha * alpha
        mask = torch.arange(r.shape[0], device=r.device) < k

        products = torch.where(mask, y * torch.roll(torch.flip(r, [0]), [k], 0),0.0)
        dot_prod = torch.sum(products)
        alpha = -(r[k] + dot_prod) / beta

        y = y.clone()
        y_update_slice = torch.where(mask, torch.roll(torch.flip(y, [0]), [k], 0) * alpha, 0.0)
        y += y_update_slice
        y[k] = alpha

        return alpha, beta, y, r
    for k in range(1,r.shape[0]):
        loop_vars = alpha, beta, y, r
        alpha, beta, y, r = loop_body(k, loop_vars)
    # _, _, y, _ = lax.fori_loop(1, r.shape[0], loop_body, (alpha, beta, y, r))

    return y


# @torch.compile()
# def inner_body(beta, alpha, y, k, r):
#     beta = beta.clone()
#     beta *= 1.0 - alpha * alpha
#     alpha = -(r[k] + torch.dot(torch.flip(r[:k], [0]), y[:k])) / beta
#     y = y.clone()
#     y[:k] += alpha * torch.flip(y[:k], [0])
#     y[k] = alpha

#     return beta, alpha, y

# def kernel(r):

#     y = torch.empty_like(r)
#     alpha = -r[0].clone()
#     beta = torch.tensor([1.0], dtype=r.dtype, device=r.device)
#     y[0] = -r[0]

#     for k in range(1, r.shape[0]):
#         k_tensor = torch.tensor([k], dtype=torch.int, device=r.device)
#         beta, alpha, y = inner_body(beta, alpha, y, k_tensor, r)

#     return y
