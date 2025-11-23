import torch

# Small dataset
# cpu backward median: 2802ms (~10% faster than non-jit compile version)
# gpu backward with @torch.jit.script median: 321ms
# gpu backward with @torch.compile(mode="max-autotune") median: 12ms, first run takes 9042ms? ~4000ms
# gpu backward with @torch.compile(mode="reduce-overhead") median: 12ms, first run takes ~4000ms
# gpu backward with @torch.compile median: 15ms, first run takes ~5000ms
# gpu backward with 2 x @torch.compile median: 3ms, first run takes ~50000ms (TMAX:20)

# Paper dataset
# gpu backward with @torch.compile median: 447ms, first run takes ~7000ms
# with clones in each loop iteration median: 267ms, first run takes ~9000ms
# JAX gpu backward median: 233ms

def kernel(TMAX, ex: torch.Tensor, ey: torch.Tensor, hz: torch.Tensor, _fict_):
    @torch.compile
    def loop_body(ex, ey, hz, fict_t):
        ey = ey.clone()
        ex = ex.clone()
        hz = hz.clone()

        ey[0, :] = fict_t
        ey[1:, :] -= 0.5 * (hz[1:, :] - hz[:-1, :])
        ex[:, 1:] -= 0.5 * (hz[:, 1:] - hz[:, :-1])
        hz[:-1, :-1] -= 0.7 * (ex[:-1, 1:] - ex[:-1, :-1] + ey[1:, :-1] - ey[:-1, :-1])

        return ex, ey, hz

    # ey = ey.clone()
    # ex = ex.clone()
    # hz = hz.clone()

    for t in range(TMAX):
        ex, ey, hz = loop_body(ex, ey, hz, _fict_[t])

    return ex, ey, hz


# Small dataset
# forward median: 300ms
# cpu backward median: 3201ms
# gpu backward median: 35ms (10 times faster than jit compiled version)
# gpu backward with @torch.compile(mode="max-autotune") median: 1ms but first run takes 122833ms
# this version doesnt validate for forward pass but backward pass is correct
# should delete clone and return for forward pass validation

# Paper dataset
# gpu backward median: 990ms

# @torch.compile(mode="max-autotune")
# def kernel(TMAX, ex: torch.Tensor, ey: torch.Tensor, hz: torch.Tensor, _fict_):

#     for t in range(TMAX):
#         ey = ey.clone()
#         ex = ex.clone()
#         hz = hz.clone()
        
#         ey[0, :] = _fict_[t]
#         ey[1:, :] -= 0.5 * (hz[1:, :] - hz[:-1, :])
#         ex[:, 1:] -= 0.5 * (hz[:, 1:] - hz[:, :-1])
#         hz[:-1, :-1] -= 0.7 * (ex[:-1, 1:] - ex[:-1, :-1] + ey[1:, :-1] -
#                                ey[:-1, :-1])

#     return ex, ey, hz