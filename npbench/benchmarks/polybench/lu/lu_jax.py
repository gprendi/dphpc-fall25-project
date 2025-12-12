import jax
import jax.numpy as jnp
from jax import lax

@jax.jit
def kernel(A):
    n = A.shape[0]

    def loop_body(A, i):
        def inner_body_1(A, j):
            # Only execute when j < i
            mask = jnp.arange(n) < j
            A_slice_1 = jnp.where(mask, A[i, :], 0.0)
            A_slice_2 = jnp.where(mask, A[:, j], 0.0)
            new_val = (A[i, j] - A_slice_1 @ A_slice_2) / A[j, j]
            updated_A = A.at[i, j].set(new_val)
            # Conditionally apply update
            A = lax.select(j < i, updated_A, A)
            return A, None

        def inner_body_2(A, j):
            # Only execute when j >= i
            mask = jnp.arange(n) < i
            A_slice_1 = jnp.where(mask, A[i, :], 0.0)
            A_slice_2 = jnp.where(mask, A[:, j], 0.0)
            new_val = A[i, j] - A_slice_1 @ A_slice_2
            updated_A = A.at[i, j].set(new_val)
            A = lax.select(j >= i, updated_A, A)
            return A, None

        A, _ = lax.scan(inner_body_1, A, jnp.arange(n))
        A, _ = lax.scan(inner_body_2, A, jnp.arange(n))
        return A, None

    A, _ = lax.scan(loop_body, A, jnp.arange(n))
    return A
