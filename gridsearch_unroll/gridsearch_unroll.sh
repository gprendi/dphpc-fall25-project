set -eou pipefail
# GRID="20 50 100 200 300 400 500 1000 1500 2000"
# GRID="$(seq 40 20 800)"
GRID="32 64 128 256 512"

for unroll in $GRID
do
    echo "Unroll factor: $unroll"
    UNROLL=$unroll TORCHINDUCTOR_FX_GRAPH_CACHE=1 \
    uv run run_benchmark.py -b go_fast -f pytorch_cpu -m backward --validate True
done