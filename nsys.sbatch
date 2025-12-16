#!/bin/bash
#SBATCH --job-name=nsys_npb
#SBATCH --account=dphpc
#SBATCH --time=06:00:00
#SBATCH --output=ad_logs/%x/%j.out
#SBATCH --error=ad_logs/%x/%j.err

echo "Starting job at $(date)"
echo "Benchmarks passed: $@"

mkdir -p nsys_reports

srun nsys profile \
  -o nsys_reports/%x_%j \
  --trace=cuda,nvtx,osrt \
  --capture-range=cudaProfilerApi \
  --capture-range-end=stop \
  --stats=true \
  python benchmark_backprop.py \
    --benchmarks "$@" \
    --frameworks pytorch_gpu \
    --preset S \
    --validate False \
    --timeout 4000


rm npbench.db