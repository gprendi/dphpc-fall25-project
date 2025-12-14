#!/bin/bash
#SBATCH --job-name=run_npb
#SBATCH --account=dphpc
#SBATCH --time=06:00:00
#SBATCH --output=ad_logs/%x/%j.out
#SBATCH --error=ad_logs/%x/%j.err

set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: sbatch benchmark_unroll.sbatch [-p PRESET] benchmark1 [benchmark2 ...]

Options:
  -p PRESET   Preset size (e.g. S, M, L). Default: M
EOF
}

PRESET="M"
while getopts ":p:h" opt; do
  case "$opt" in
    p)
      PRESET="$OPTARG"
      ;;
    h)
      usage
      exit 0
      ;;
    \?)
      echo "Error: unknown option -$OPTARG" >&2
      usage
      exit 2
      ;;
    :)
      echo "Error: option -$OPTARG requires an argument" >&2
      usage
      exit 2
      ;;
  esac
done
shift $((OPTIND - 1))

if [ "$#" -eq 0 ]; then
  echo "Error: no benchmarks passed" >&2
  usage
  exit 1
fi

echo "Starting job at $(date)"
echo "Benchmarks passed: $@"

echo "Preset: $PRESET"

BENCH_TAG="${*// /_}"
FOLDER="unroll-${BENCH_TAG}-${PRESET}"
mkdir -p "$FOLDER"

rm -f npbench.db
UNROLL=1 srun --ntasks=1 python benchmark_backprop.py -b "$@" -f jax_gpu pytorch_gpu --preset "$PRESET"
mv -f npbench.db "${FOLDER}/npbench-baseline.db"

# GRID="16 24 32 48 64 96 128 192 256 384 512 768 1024"

# for unroll in $GRID
# do
#     rm -f npbench.db
#     echo "Unroll factor: $unroll"
#     UNROLL=$unroll TORCHINDUCTOR_FX_GRAPH_CACHE=1 \
#     srun --ntasks=1 python benchmark_backprop.py -b "$@" -f pytorch_gpu --preset $PRESET
#     mv -f npbench.db "${FOLDER}/npbench-unroll-$unroll.db"
# done
