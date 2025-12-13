import jax
import jax.numpy as jnp
from jax import lax

@jax.jit
def kernel(A):
    n = A.shape[0]
    A = A.at[0, 0].set(jnp.sqrt(A[0, 0]))

    def row_step(A, i):
        # inner scan over all j, no-ops when j >= i
        def col_step(A, j):
            mask = j < i
            a_i = jnp.where(mask, A[i, :], 0)
            a_j = jnp.where(mask, A[j, :], 0)
            dot = jnp.dot(a_i, a_j)
            upd = (A[i, j] - dot) / A[j, j]
            A = A.at[i, j].set(jnp.where(mask, upd, A[i, j]))
            return A, None  # carry, unused output

        A, _ = lax.scan(col_step, A, jnp.arange(n))

        a_i = jnp.where(jnp.arange(n) < i, A[i, :], 0)
        dot = jnp.dot(a_i, a_i)
        A = A.at[i, i].set(jnp.sqrt(A[i, i] - dot))
        return A, None  # carry, unused output

    A, _ = lax.scan(row_step, A, jnp.arange(1, n))
    return A
