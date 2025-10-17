import torch

def stockham_fft_pytorch(N, R, K, x, y):
    X_torch = torch.tensor(torch.from_numpy(x), dtype=torch.complex128)
    Y_torch = torch.tensor(torch.from_numpy(y), dtype=torch.complex128)
    t_r = torch.arange(R)

    i_coord, j_coord = torch.meshgrid(torch.arange(R), torch.arange(R), indexing='ij')
    # dft_mat = torch.empty((R,R), dtype=torch.complex128)
    dft_mat = torch.exp(-2.0j * torch.pi * i_coord * j_coord / R)
    dft_mat = torch.tensor(dft_mat, dtype=torch.complex128)
    Y_torch[:] = X_torch[:]

    ii_coord, jj_coord = torch.meshgrid(torch.arange(R), torch.arange(R ** K), indexing='ij')

    for i in range(K):
        # Stride permutation
        # yv = np.reshape(y, (R**i, R, R**(K - i - 1)))
        yv = torch.reshape(Y_torch, (R ** i, R, R ** (K - i - 1)))

        # tmp_perm = np.transpose(yv, axes=(1, 0, 2))
        tmp_perm = torch.permute(yv, (1, 0, 2))

        # Twiddle Factor multiplication
        # D = np.empty((R, R**i, R**(K - i - 1)), dtype=np.complex128)
        D = torch.empty((R, R ** i, R ** (K - i - 1)), dtype=torch.complex128)

        # tmp = np.exp(-2.0j * np.pi * ii_coord[:, :R**i] * jj_coord[:, :R**i] /
        #  R**(i + 1))
        tmp = torch.exp(-2.0j * torch.pi * ii_coord[:, :R ** i] * jj_coord[:, :R ** i] / R ** (i + 1))

        # D[:] = np.repeat(np.reshape(tmp, (R, R**i, 1)), R**(K - i - 1), axis=2)
        tmp_reshaped = torch.reshape(tmp, (R, R ** i, 1))
        D[:] = torch.repeat_interleave(tmp_reshaped, R ** (K - i - 1), dim=2)

        # tmp_twid = np.reshape(tmp_perm, (N, )) * np.reshape(D, (N, ))
        tmp_twid = torch.reshape(tmp_perm, (N,)) * torch.reshape(D, (N,))

        # Product with Butterfly
        # y[:] = np.reshape(dft_mat @ np.reshape(tmp_twid, (R, R**(K - 1))),
        #                   (N, ))
        tmp_twid_reshaped = torch.reshape(tmp_twid, (R, R ** (K - 1)))

        Y_torch[:] = torch.reshape(torch.matmul(dft_mat, tmp_twid_reshaped), (N,))
        y[:] = Y_torch[:]