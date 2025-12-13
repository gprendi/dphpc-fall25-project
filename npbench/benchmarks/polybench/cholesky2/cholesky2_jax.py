import jax
import jax.numpy as jnp

@jax.jit
def kernel(A: jax.Array):
    return jnp.linalg.cholesky(A) + jnp.triu(A, k=1)
