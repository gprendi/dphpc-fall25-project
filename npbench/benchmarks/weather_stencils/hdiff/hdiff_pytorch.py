import torch

def hdiff(in_field: torch.Tensor, out_field: torch.Tensor, coeff: torch.Tensor) -> torch.Tensor:
    I, J, K = out_field.shape[0], out_field.shape[1], out_field.shape[2]
    lap_field = 4.0 * in_field[1:I + 3, 1:J + 3, :] - (
        in_field[2:I + 4, 1:J + 3, :] + in_field[0:I + 2, 1:J + 3, :] +
        in_field[1:I + 3, 2:J + 4, :] + in_field[1:I + 3, 0:J + 2, :])

    res = lap_field[1:, 1:J + 1, :] - lap_field[:-1, 1:J + 1, :]
    flx_field = torch.where(
        (res *
         (in_field[2:I + 3, 2:J + 2, :] - in_field[1:I + 2, 2:J + 2, :])) > 0,
        torch.tensor(0.0, dtype=res.dtype, device=res.device),
        res,
    )

    res = lap_field[1:I + 1, 1:, :] - lap_field[1:I + 1, :-1, :]
    fly_field = torch.where(
        (res *
         (in_field[2:I + 2, 2:J + 3, :] - in_field[2:I + 2, 1:J + 2, :])) > 0,
        torch.tensor(0.0, dtype=res.dtype, device=res.device),
        res,
    )

    # Relative error: ~0.8
    # out_field[:, :, :] = in_field[2:I + 2, 2:J + 2, :] - coeff[:, :, :] * (
    #     flx_field[1:, :, :] - flx_field[:-1, :, :] + fly_field[:, 1:, :] -
    #     fly_field[:, :-1, :])
    # return out_field

    # SUCCESS
    result = in_field[2:I + 2, 2:J + 2, :] - coeff[:, :, :] * (
        flx_field[1:, :, :] - flx_field[:-1, :, :] + fly_field[:, 1:, :] -
        fly_field[:, :-1, :])

    return result

    # Relative error: ~0.8
    # if out_field.requires_grad:
    #     return result
    # out_field.copy_(result)
    # return out_field