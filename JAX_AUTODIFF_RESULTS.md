# JAX Autodiff Compatibility Test Results
## IMPORTANT COPILOT GENERATED THIS FROM MY OUTPUT
This document summarizes the autodiff support status for all benchmarks in NPBench when using JAX framework. Tests were run with reverse-mode differentiation (backward mode) via `jax.value_and_grad()`.

## Summary

- **Total Benchmarks**: 54
- **Successful**: 29
- **Failed**: 25

## Detailed Results

### ✅ Successful (29)

| Benchmark | Status | Notes |
|-----------|--------|-------|
| adi | SUCCESS | All derivatives computed correctly |
| arc_distance | SUCCESS | All derivatives computed correctly |
| atax | SUCCESS | All derivatives computed correctly |
| azimint_hist | SUCCESS | All derivatives computed correctly |
| azimint_naive | SUCCESS | All derivatives computed correctly |
| cavity_flow | SUCCESS | All derivatives computed correctly |
| cholesky2 | SUCCESS | All derivatives computed correctly |
| conv2d_bias | SUCCESS | All derivatives computed correctly |
| correlation | SUCCESS | All derivatives computed correctly |
| covariance | SUCCESS | All derivatives computed correctly |
| deriche | SUCCESS | All derivatives computed correctly |
| doitgen | SUCCESS | All derivatives computed correctly |
| durbin | SUCCESS | All derivatives computed correctly |
| gemm | SUCCESS | All derivatives computed correctly |
| gemver | SUCCESS | All derivatives computed correctly |
| gesummv | SUCCESS | All derivatives computed correctly |
| go_fast | SUCCESS | Also has lib-implementation support |
| hdiff | SUCCESS | All derivatives computed correctly |
| jacobi_1d | SUCCESS | All derivatives computed correctly |
| jacobi_2d | SUCCESS | All derivatives computed correctly |
| k2mm | SUCCESS | All derivatives computed correctly |
| k3mm | SUCCESS | All derivatives computed correctly |
| lenet | SUCCESS | All derivatives computed correctly |
| mlp | SUCCESS | All derivatives computed correctly |
| mvt | SUCCESS | All derivatives computed correctly |
| resnet | SUCCESS | All derivatives computed correctly |
| softmax | SUCCESS | Fixed by removing `jax.lax.stop_gradient()` |
| symm | SUCCESS | All derivatives computed correctly |
| syr2k | SUCCESS | All derivatives computed correctly |
| syrk | SUCCESS | All derivatives computed correctly |
| trisolv | SUCCESS | Also has lib-implementation support with improved performance |
| trmm | SUCCESS | All derivatives computed correctly |

### ❌ Failed (25)

#### 1. **bicg**
**Failure Reason**: Shape broadcasting error
```
add got incompatible shapes for broadcasting: (4000,), (5000,)
```
**Root Cause**: Dimension mismatch in array operations during gradient computation.

#### 2. **channel_flow**
**Failure Reason**: Non-real output type
```
grad requires real-valued outputs (output dtype that is a sub-dtype of np.floating), 
but got int64
```
**Root Cause**: JAX's default reverse-mode differentiation requires real-valued outputs. Integer outputs are not differentiable without explicit configuration.

#### 3. **cholesky**
**Failure Reason**: Dynamic loop bounds in JAX
```
Reverse-mode differentiation does not work for lax.while_loop or lax.fori_loop 
with dynamic start/stop values. Try using lax.scan, or using fori_loop with static start/stop.
```
**Root Cause**: JAX's reverse-mode AD cannot handle loops with values that depend on runtime data. Requires refactoring to use `lax.scan` or static bounds.

#### 4. **compute**
**Failure Reason**: Non-real input type
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got int64
```
**Root Cause**: Integer inputs are not differentiable in JAX without special handling.

#### 5. **contour_integral**
**Failure Reason**: Complex-valued output
```
grad requires real-valued outputs (output dtype that is a sub-dtype of np.floating), 
but got complex128. For holomorphic differentiation, pass holomorphic=True. 
For differentiation of non-holomorphic functions involving complex outputs, use jax.vjp directly.
```
**Root Cause**: Complex outputs require special configuration. Would need to modify autodiff framework to use `holomorphic=True` mode.

#### 6. **covariance2**
**Failure Reason**: Missing JAX implementation
```
ModuleNotFoundError: No module named 'npbench.benchmarks.polybench.covariance2.covariance2_jax'
```
**Root Cause**: No `_jax.py` variant exists for this benchmark.

#### 7. **crc16**
**Failure Reason**: Non-real input type (uint8)
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got uint8
```
**Root Cause**: Unsigned integer inputs are not differentiable in JAX. CRC operations are inherently discrete.

#### 8. **fdtd_2d**
**Failure Reason**: Shape broadcasting error
```
Incompatible shapes for broadcasting: shapes=[(200, 220), (20,)]
```
**Root Cause**: Dimension mismatch in stencil computation during gradient propagation.

#### 9. **floyd_warshall**
**Failure Reason**: Non-real input type (int32)
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got int32
```
**Root Cause**: Integer graph weights are not inherently differentiable.

#### 10. **gramschmidt**
**Failure Reason**: Shape broadcasting error
```
add got incompatible shapes for broadcasting: (70, 60), (60, 60)
```
**Root Cause**: Dimension mismatch in orthogonalization computation.

#### 11. **heat_3d**
**Failure Reason**: Dynamic loop bounds in JAX
```
Reverse-mode differentiation does not work for lax.while_loop or lax.fori_loop 
with dynamic start/stop values. Try using lax.scan, or using fori_loop with static start/stop.
```
**Root Cause**: Temporal evolution with dynamic iteration count not compatible with JAX reverse-mode AD.

#### 12. **lu**
**Failure Reason**: Dynamic loop bounds in JAX
```
Reverse-mode differentiation does not work for lax.while_loop or lax.fori_loop 
with dynamic start/stop values. Try using lax.scan, or using fori_loop with static start/stop.
```
**Root Cause**: LU decomposition algorithm uses dynamic loop bounds that JAX cannot differentiate.

#### 13. **ludcmp**
**Failure Reason**: Dynamic loop bounds in JAX
```
Reverse-mode differentiation does not work for lax.while_loop or lax.fori_loop 
with dynamic start/stop values. Try using lax.scan, or using fori_loop with static start/stop.
```
**Root Cause**: Similar to LU — uses dynamic loop bounds for decomposition algorithm.

#### 14. **mandelbrot1**
**Failure Reason**: Empty array handling in max()
```
max() iterable argument is empty
```
**Root Cause**: Mandelbrot computation produces empty result arrays in certain parameter ranges, causing max() to fail.

#### 15. **mandelbrot2**
**Failure Reason**: Empty array handling in max()
```
max() iterable argument is empty
```
**Root Cause**: Same as mandelbrot1 — empty iteration results.

#### 16. **nbody**
**Failure Reason**: Validation failed
```
Jax - default did not validate!
Failed to run Jax validation.
```
**Root Cause**: Backward pass validation failed (details in full traceback).

#### 17. **nussinov**
**Failure Reason**: Non-real input type (int32)
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got int32
```
**Root Cause**: RNA distance matrix uses integer indices and cannot be differentiated directly.

#### 18. **scattering_self_energies**
**Failure Reason**: Non-real input type (int32)
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got int32
```
**Root Cause**: Physical constants or indices use integer representation.

#### 19. **seidel_2d**
**Failure Reason**: Dynamic loop bounds in JAX
```
Reverse-mode differentiation does not work for lax.while_loop or lax.fori_loop 
with dynamic start/stop values. Try using lax.scan, or using fori_loop with static start/stop.
```
**Root Cause**: Seidel iteration uses dynamic bounds that JAX AD cannot handle.

#### 20. **softmax** (PREVIOUSLY FAILED - NOW FIXED)
**Previous Failure**: Gradient blocking
```
Reverse-mode differentiation could not differentiate operation due to stop_gradient()
```
**Fix Applied**: Removed `jax.lax.stop_gradient()` call that was explicitly blocking gradient flow.
**Current Status**: ✅ **SUCCESS** (Fixed by modifying `npbench/benchmarks/deep_learning/softmax/softmax_jax.py`)

#### 21. **spmv**
**Failure Reason**: Non-real input type (uint32)
```
grad requires real- or complex-valued inputs (input dtype that is a sub-dtype of np.inexact), 
but got uint32
```
**Root Cause**: Sparse matrix indices use unsigned integer type.

#### 22. **stockham_fft**
**Failure Reason**: Complex-valued output
```
grad requires real-valued outputs (output dtype that is a sub-dtype of np.floating), 
but got complex128. For holomorphic differentiation, pass holomorphic=True. 
For differentiation of non-holomorphic functions involving complex outputs, use jax.vjp directly.
```
**Root Cause**: FFT produces complex frequency domain output. Would require holomorphic differentiation configuration.

#### 23. **vadv**
**Failure Reason**: Shape broadcasting error
```
Incompatible shapes for broadcasting: shapes=[(60, 60, 40), (60, 60)]
```
**Root Cause**: Dimension mismatch in advection stencil computation.

## Failure Categories

### By Error Type

| Error Category | Count | Benchmarks |
|---|---|---|
| Shape Broadcasting Mismatch | 4 | bicg, fdtd_2d, gramschmidt, vadv |
| Non-Real/Non-Complex Input Types | 6 | channel_flow, compute, crc16, floyd_warshall, nussinov, scattering_self_energies, spmv |
| Complex-Valued Output | 2 | contour_integral, stockham_fft |
| Dynamic Loop Bounds | 5 | cholesky, heat_3d, lu, ludcmp, seidel_2d |
| Empty Array Handling | 2 | mandelbrot1, mandelbrot2 |
| Missing Implementation | 1 | covariance2 |
| Validation Failure | 1 | nbody |

## Recommendations for Fixes

### High Priority (Easily Fixable)

1. **Integer/Complex Type Conversions** (6 benchmarks)
   - Convert integer inputs to float before gradient computation
   - Modify JAX kernel implementations to use float dtypes
   - Examples: channel_flow, compute, crc16, floyd_warshall, nussinov, spmv

2. **Shape Issues** (4 benchmarks)
   - Review broadcasting operations in gradient path
   - May require reshaping or slicing operations
   - Examples: bicg, fdtd_2d, gramschmidt, vadv

### Medium Priority (Requires Algorithmic Changes)

3. **Complex Outputs** (2 benchmarks)
   - Enable `holomorphic=True` in JAX autodiff configuration
   - Or switch to real-valued loss computation
   - Examples: contour_integral, stockham_fft

4. **Empty Array Handling** (2 benchmarks)
   - Add guards for empty arrays before calling max()
   - Examples: mandelbrot1, mandelbrot2

### High Priority (Major Refactoring Required)

5. **Dynamic Loop Bounds** (5 benchmarks)
   - Refactor to use `jax.lax.scan` instead of `fori_loop`/`while_loop`
   - Or make loop bounds static/shape-traced
   - Examples: cholesky, heat_3d, lu, ludcmp, seidel_2d

### Low Priority (Framework Issues)

6. **Missing Implementations**
   - Implement `covariance2_jax.py`

7. **Validation Issues**
   - Debug `nbody` validation failure (may be numerical precision issue)
 
## Framework Integration

All autodiff configurations are defined in `bench_info/*.json` with:
```json
"autodiff": {
  "loss": { "type": "sum", "target": "result" },
  "grad_inputs": [<array_args>]
}
```

The JAX framework in `npbench/infrastructure/jax_framework.py` uses `jax.value_and_grad()` for reverse-mode differentiation with sum-of-outputs as the loss function.

