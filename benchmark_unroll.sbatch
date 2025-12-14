#!/bin/bash
#SBATCH --job-name=run_npb
#SBATCH --account=dphpc
#SBATCH --time=06:00:00
#SBATCH --output=ad_logs/%x/%j.out
#SBATCH --error=ad_logs/%x/%j.err

set -euo pipefail

echo "Starting job at $(date)"
echo "Benchmarks passed: $@"

# srun python benchmark_backprop.py \
#     --benchmarks $@ \
#     --frameworks jax_cpu jax_gpu pytorch_gpu \
#     --preset M \
#     --validate True \
#     --timeout 4000

# echo "Finished job at $(date)"


GRID="16 24 32 48 64 96 128 192 256 384 512 768 1024"

for unroll in $GRID
do
    rm -f npbench.db
    echo "Unroll factor: $unroll"
    UNROLL=$unroll TORCHINDUCTOR_FX_GRAPH_CACHE=1 \
    srun python benchmark_backprop.py -b $@ -f pytorch_gpu --preset S
    mv -n npbench.db npbench-unroll-$unroll.db
done
