#!/bin/bash

set -e

echo "=== Pink Morsels Sales Visualizer - Test Suite ==="
echo ""

echo "Step 1: Activating virtual environment..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "✗ Error: Virtual environment not found at .venv/"
    exit 1
fi

echo ""
echo "Step 2: Running test suite..."
echo ""

if python -m pytest test_appv1.py -v; then
    echo ""
    echo "==================================="
    echo "✓ All tests passed successfully!"
    echo "==================================="
    exit 0
else
    echo ""
    echo "==================================="
    echo "✗ Tests failed!"
    echo "==================================="
    exit 1
fi
