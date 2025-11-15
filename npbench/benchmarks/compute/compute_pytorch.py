import torch

@torch.compile
def compute(array_1: torch.Tensor, array_2: torch.Tensor, a: float, b: float, c: float) -> torch.Tensor:
    return torch.clip(array_1, 2.0, 10.0) * a + array_2 * b + c