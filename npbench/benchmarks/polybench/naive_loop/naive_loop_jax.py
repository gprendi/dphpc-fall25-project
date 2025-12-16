import jax
import jax.numpy as jnp
from jax import lax
from functools import partial

@partial(jax.jit, static_argnums=(0,))
def kernel(M, data):
    data = jnp.asarray(data)

    def loop_body(i, arr):
        return arr.at[i].set(1.0)

    result = lax.fori_loop(0, M, loop_body, data)
    return result
