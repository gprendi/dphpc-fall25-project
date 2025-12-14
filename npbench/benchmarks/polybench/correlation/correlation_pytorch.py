import torch

# ---------CPU forward---------Pytorch  vs Jax
# S dataset cpu forward median:  59ms      4ms
# paper data cpu forward median: 167ms    196ms

# ---------CPU backward---------Pytorch  vs Jax
# S dataset cpu backward median:  199ms   6ms
# paper data cpu backward median: 1665ms 346ms

# ---------GPU backward---------Pytorch  vs Jax
# S dataset cpu backward median:  115ms     3ms
# paper data cpu backward median: 294ms    25ms

def kernel(M, float_n, data):
    @torch.compile
    def loop_body(i_tensor, corr):
        corr[i_tensor, i_tensor] = 1.0
        return corr
    
    mean = torch.mean(data, dim=0)
    stddev = torch.std(data, dim=0, correction=0)
    stddev = torch.where(stddev <= 0.1, torch.ones_like(stddev), stddev)
    data = data - mean
    data = data / (torch.sqrt(torch.tensor(float_n, dtype=data.dtype, device=data.device)) * stddev)
    corr = torch.matmul(data.T, data)
    
    for i in range(M):
        i_tensor = torch.tensor([[i]], dtype=torch.int32, device=data.device)  # shape (1, 1)
        corr = loop_body(i_tensor, corr)
    
    return corr

# ---------CPU forward---------Pytorch  vs Jax
# S dataset cpu forward median: 240ms      4ms
# M dataset cpu forward median: 512ms     296ms
# L dataset cpu forward median: 2425ms    1768ms
# paper data cpu forward median: 392ms    196ms

# ---------CPU backward---------Pytorch  vs Jax
# S dataset cpu backward median:  23065ms   6ms
# M dataset cpu backward median:  timed out 499ms
# paper data cpu backward median: timed out 346ms

# ---------GPU backward---------Pytorch  vs Jax
# S dataset cpu backward median:   38ms     3ms
# paper data cpu backward median:  101ms    25ms

# def kernel(M, float_n, data):
#     @torch.compile
#     def loop_body(i, corr):
#         corr[i, i] = 1.0
#         return corr
    
#     mean = torch.mean(data, dim=0)
#     stddev = torch.std(data, dim=0, correction=0)
#     stddev = torch.where(stddev <= 0.1, torch.ones_like(stddev), stddev)
#     data = data - mean
#     data = data / (torch.sqrt(torch.tensor(float_n, dtype=data.dtype)) * stddev)
#     corr = torch.matmul(data.T, data)
    
#     for i in range(M):
#         corr = loop_body(i, corr)
    
#     return corr

# works with S dataset but times out with M dataset
# S dataset cpu forward median: 3092ms
# M dataset cpu forward median: does not compile

# @torch.compile
# def kernel(M, float_n, data):
#     mean = torch.mean(data, dim=0)
#     stddev = torch.std(data, dim=0, correction=0)
#     stddev = torch.where(stddev <= 0.1, torch.ones_like(stddev), stddev)
#     data = data - mean
#     data = data / (torch.sqrt(torch.tensor(float_n, dtype=data.dtype)) * stddev)
#     corr = torch.matmul(data.T, data)

#     for i in range(M):
#         corr[i, i] = 1.0

#     return corr
