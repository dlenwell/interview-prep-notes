#!/usr/bin/env bash

set -u

if [[ $# -ne 1 || ! -d "$1" ]]; then
    echo "Usage: $0 problems/word-pattern"
    exit 1
fi

PROBLEM_DIR="$(cd "$1" && pwd)"

run_tests() {
    echo
    echo "========================================"
    echo "Testing: $PROBLEM_DIR"
    echo "========================================"

    echo "--- Lint ---"
    ruff check "$PROBLEM_DIR/solution.py"

    echo "--- Unit tests ---"
    python3 -m unittest discover \
        -s "$PROBLEM_DIR" \
        -p 'test_*.py' \
        -v

    echo "--- Run solution ---"
    python3 "$PROBLEM_DIR/solution.py"
}

# Run immediately
run_tests

# Watch for changes and rerun
if ! command -v entr >/dev/null 2>&1; then
    echo "Error: entr is not installed (brew install entr)"
    exit 1
fi

export PROBLEM_DIR
export -f run_tests

echo
echo "Watching for changes. Press Ctrl+C to stop."
trap 'exit 130' INT
while true; do
    find "$PROBLEM_DIR" -name '*.py' | \
        entr -d -c bash -c 'run_tests'
done
