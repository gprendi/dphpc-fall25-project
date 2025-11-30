import torch

def kernel(L, x, b):
    @torch.compile
    def loop_body(i, loop_vars):
        L, x, b = loop_vars
        mask = torch.arange(x.shape[0], device=x.device) < i
        products = torch.where(mask, L[i, :] * x, torch.tensor(0.0, dtype=x.dtype, device=x.device))
        dot_product = torch.sum(products)
        x = x.clone()  # Create a new tensor for immutable-style update
        x[i] = (b[i] - dot_product) / L[i, i]
        return L, x, b
    
    for i in range(x.shape[0]):
        L, x, b = loop_body(i, (L, x, b))
    
    return x