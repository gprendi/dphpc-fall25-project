#!/bin/bash
#SBATCH --job-name=run_npb
#SBATCH --account=dphpc
#SBATCH --time=06:00:00
#SBATCH --output=ad_logs/%x_%j.out
#SBATCH --error=ad_logs/%x_%j.err

echo "Starting job at $(date)"
echo "Benchmarks passed: $@"

srun python benchmark_backprop.py \
    --benchmarks $@ \
    --frameworks jax_cpu jax_gpu pytorch_cpu pytorch_gpu \
    --preset paper \
    --validate False

echo "Finished job at $(date)"
