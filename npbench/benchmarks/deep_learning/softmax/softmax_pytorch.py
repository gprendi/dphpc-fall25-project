import torch

def softmax(x):
    tmp_max = torch.max(x, dim=-1, keepdim=True).values
    tmp_max = tmp_max.detach() # stop gradient
    x = torch.exp(x - tmp_max)
    denominator = torch.sum(x, dim=-1, keepdim=True)
    return x / denominator