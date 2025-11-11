import torch


def go_fast(a: torch.Tensor) -> torch.Tensor:
    trace = torch.tanh(torch.diagonal(a)).sum()
    return a + trace
