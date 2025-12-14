import jax
import jax.numpy as jnp
from jax import lax


@jax.jit
def kernel(A):
    n = A.shape[0]
    A = A.at[0, 0].set(jnp.sqrt(A[0, 0]))

    def row_step(A, i):
        def col_step(A, j):
            # Only update entries strictly below the diagonal (j < i)
            def do_update(A):
                mask = jnp.arange(n) < j
                a_i = jnp.where(mask, A[i, :], 0)
                a_j = jnp.where(mask, A[j, :], 0)
                dot = jnp.dot(a_i, a_j)
                val = (A[i, j] - dot) / A[j, j]
                return A.at[i, j].set(val)

            return lax.cond(j < i, do_update, lambda x: x, A), None

        A, _ = lax.scan(col_step, A, jnp.arange(n))

        mask = jnp.arange(n) < i
        a_i = jnp.where(mask, A[i, :], 0)
        dot = jnp.dot(a_i, a_i)
        A = A.at[i, i].set(jnp.sqrt(A[i, i] - dot))
        return A, None

    A, _ = lax.scan(row_step, A, jnp.arange(1, n))
    return A
