#!/bin/bash
#SBATCH --job-name=run_npb
#SBATCH --account=dphpc
#SBATCH --time=06:00:00
#SBATCH --output=ad_logs/%x/%j.out
#SBATCH --error=ad_logs/%x/%j.err

echo "Starting job at $(date)"
echo "Benchmarks passed: $@"

srun python benchmark_backprop.py \
    --benchmarks $@ \
    --frameworks jax_cpu jax_gpu pytorch_cpu pytorch_gpu \
    --preset S \
    --validate True \
    --timeout 4000

mv npbench.db npbench_compile_S_both.db

echo "Finished job at $(date)"
