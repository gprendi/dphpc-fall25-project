import torch

@torch.compile
def kernel(NR, NQ, NP, A: torch.Tensor, C4: torch.Tensor) -> torch.Tensor:  
    A_new = A @ C4   
    return A_new