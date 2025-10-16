#!/usr/bin/env bash
# =========================================================
# run_tests.sh — Execute pytest test suites for this project
# =========================================================
# This script runs all test files and reports detailed results.
# Usage:
#   ./run_tests.sh
# =========================================================

# Exit immediately if any command fails
set -e

echo "======================================="
echo "Running Python test suite with pytest..."
echo "======================================="

# Run all test files explicitly (or simply 'pytest tests/' if you have a folder)
pytest -v \
    test_math_utils.py \
    test_bank_account.py \
    test_bank_account_mocked.py

echo "======================================="
echo "✅ All test"
