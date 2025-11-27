import jax
import jax.numpy as jnp
from functools import partial

@partial(jax.jit, static_argnums=(1, 2))
def kernel(A, row, column):

    Q = jnp.zeros_like(A)
    R = jnp.zeros((column, column), dtype=A.dtype)

    def body_fun(k, arrays):
        Q, R, A = arrays

        nrm = jnp.dot(A[:, k], A[:, k])
        R = R.at[k, k].set(jnp.sqrt(nrm))
        Q = Q.at[:, k].set(A[:, k] / R[k, k])

        def inner_body_fun(j, arrays):
            Q, R, A = arrays

            def update(arrays):
                Q, R, A = arrays
                r = jnp.dot(Q[:, k], A[:, j])
                R = R.at[k, j].set(r)
                A = A.at[:, j].add(-Q[:, k] * r)
                return Q, R, A

            return jax.lax.cond(j > k, update, lambda arrays: arrays, (Q, R, A))

        Q, R, A = jax.lax.fori_loop(0, column, inner_body_fun, (Q, R, A))
        return Q, R, A

    Q, R, A = jax.lax.fori_loop(0, column, body_fun, (Q, R, A))

    return Q, R
