#!/usr/bin/env bash

# Usage: ./run_autodiff_backprop.sh [options] [-- extra run_benchmark.py args]
# Options:
#   -f, --framework NAME    Framework to benchmark (default: ${FRAMEWORK})
#   -p, --preset PRESET     NPBench preset S|M|L|paper (default: ${PRESET})
#   -r, --repeat N          Number of repeats per benchmark (default: ${REPEAT})
#   -t, --timeout SECONDS   Timeout for each benchmark (default: ${TIMEOUT})
#   -v, --validate BOOL     Whether to validate results (default: ${VALIDATE})
#   -h, --help              Show this help message
# Automatically discovers autodiff benchmarks and runs each in backward mode (run_benchmark.py).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODES=("forward" "backward")
FRAMEWORK="pytorch_cpu"
PRESET="S"
REPEAT=2
TIMEOUT=200
VALIDATE="true"
EXTRA_ARGS=()

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is required to run this script. Please install uv: https://docs.astral.sh/uv/" >&2
    exit 1
fi

UV_PYTHON=(uv run --no-sync python)

while [[ $# -gt 0 ]]; do
    case "$1" in
        -f|--framework) FRAMEWORK="$2"; shift 2 ;;
        -p|--preset) PRESET="$2"; shift 2 ;;
        -r|--repeat) REPEAT="$2"; shift 2 ;;
        -t|--timeout) TIMEOUT="$2"; shift 2 ;;
        -v|--validate) VALIDATE="$2"; shift 2 ;;
        --) shift; EXTRA_ARGS+=("$@"); break ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

AUTODIFF_ROWS=()
while IFS= read -r line; do
    [[ -z "${line}" ]] && continue
    AUTODIFF_ROWS+=("${line}")
done < <(
    "${UV_PYTHON[@]}" - "$REPO_ROOT" <<'PY'
import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
bench_dir = root / "bench_info"
records = []
for path in sorted(bench_dir.glob("*.json")):
    with path.open() as fh:
        try:
            data = json.load(fh)
        except json.JSONDecodeError:
            continue
    bench = data.get("benchmark", {})
    if "autodiff" not in bench:
        continue
    records.append((path.stem, bench.get("short_name", path.stem), bench.get("name", path.stem)))

for record in records:
    print("|".join(record))
PY
)

if [[ ${#AUTODIFF_ROWS[@]} -eq 0 ]]; then
    echo "No benchmarks with autodiff metadata were found."
    exit 0
fi

BENCHES=()
for row in "${AUTODIFF_ROWS[@]}"; do
    IFS="|" read -r bench_id short_name full_name <<< "${row}"
    echo " - ${bench_id} (short: ${short_name}) — ${full_name}"
    BENCHES+=("${bench_id}")
done

echo
for mode in "${MODES[@]}"; do
    echo "Autodiff-enabled benchmarks (will run in $mode mode):"
    for bench in "${BENCHES[@]}"; do
        echo ">>> Running ${bench}..."
        CMD=("${UV_PYTHON[@]}" "${REPO_ROOT}/run_benchmark.py"
            -b "${bench}"
            -f "${FRAMEWORK}"
            -m "${mode}"
            -p "${PRESET}"
            -r "${REPEAT}"
            -t "${TIMEOUT}"
            -v "${VALIDATE}")
        if [[ ${#EXTRA_ARGS[@]} -gt 0 ]]; then
            CMD+=("${EXTRA_ARGS[@]}")
        fi
        "${CMD[@]}"
        echo
    done
done
