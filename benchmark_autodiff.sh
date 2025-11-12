#!/usr/bin/env bash


# Simple benchmarking script for autodiff (backprop and forward)
# Runs: pytorch_cpu, pytorch_gpu, jax
# Sizes: S (20 runs), M (10 runs), L (10 runs)
# Modes: backward, forward

set -euo pipefail


FRAMEWORKS=(pytorch_cpu pytorch_gpu jax)
SIZES=(S M L)
REPEATS=(20 10 10)
MODES=(backward forward)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"


for mode in "${MODES[@]}"; do
    for fw in "${FRAMEWORKS[@]}"; do
        for i in "${!SIZES[@]}"; do
            size="${SIZES[$i]}"
            repeat="${REPEATS[$i]}"
            echo "==== Benchmarking $fw size $size ($repeat runs) mode: $mode ===="
            bash "$SCRIPT_DIR/run_autodiff_backprop.sh" -f "$fw" -p "$size" -r "$repeat" -m "$mode"
        done
    done
done
