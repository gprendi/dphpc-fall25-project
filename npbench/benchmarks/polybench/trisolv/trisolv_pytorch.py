import torch

def kernel(L, x, b):
    @torch.compile
    def loop_body(i_tensor, loop_vars):
        L, x, b = loop_vars
        mask = torch.arange(x.shape[0], device=x.device) < i_tensor
        products = torch.where(mask, L[i_tensor, :] * x, torch.tensor(0.0, dtype=x.dtype, device=x.device))
        dot_product = torch.sum(products)
        x = x.clone()
        x[i_tensor] = (b[i_tensor] - dot_product) / L[i_tensor, i_tensor]
        return L, x, b
    
    for i in range(x.shape[0]):
        i_tensor = torch.tensor(i, dtype=torch.int32, device=x.device)  # Just a scalar tensor
        L, x, b = loop_body(i_tensor, (L, x, b))
    
    return x


# with constant i: hit config.recompile_limit
# def kernel(L, x, b):
#     @torch.compile
#     def loop_body(i, loop_vars):
#         L, x, b = loop_vars
#         mask = torch.arange(x.shape[0], device=x.device) < i
#         products = torch.where(mask, L[i, :] * x, torch.tensor(0.0, dtype=x.dtype, device=x.device))
#         dot_product = torch.sum(products)
#         x = x.clone()  # Create a new tensor for immutable-style update
#         x[i] = (b[i] - dot_product) / L[i, i]
#         return L, x, b
    
#     for i in range(x.shape[0]):
#         L, x, b = loop_body(i, (L, x, b))
    
#     return x