#!/bin/sh
set -eu
cd "$(dirname "$0")"
PYTHON=${PYTHON:-python3}
"$PYTHON" checks/exact_checks.py
"$PYTHON" checks/bernstein_certificate.py
"$PYTHON" checks/positive_kernel_algebra.py
"$PYTHON" checks/positive_kernel_diagnostics.py
"$PYTHON" checks/direct_continuation_algebra.py > checks/DIRECT_ALGEBRA_CHECKS.txt
"$PYTHON" checks/full_circle_diagnostics.py > checks/FULL_CIRCLE_DIAGNOSTICS.json
"$PYTHON" checks/measure_moments.py
