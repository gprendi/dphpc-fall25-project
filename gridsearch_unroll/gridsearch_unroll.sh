set -eou pipefail
# GRID="10 20 50 100 200 300 400 500 1000 1500 2000"
# GRID="$(seq 40 20 800)"
# GRID="32 64 128 256 512"
GRID="16 24 32 48 64 96 128 192 256 384 512 768 1024 1536 2048"

for unroll in $GRID
do
    echo "Unroll factor: $unroll"
    UNROLL=$unroll TORCHINDUCTOR_FX_GRAPH_CACHE=1 \
    python run_benchmark.py -b go_fast -f pytorch_gpu -m backward --preset M
    mv npbench.db npbench-unroll-$unroll.db
done