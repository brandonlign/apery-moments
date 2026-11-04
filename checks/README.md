# Verification code

Supplemental material for Brandon Li, *Stieltjes moment classification of
Apéry polynomials*. Contact: brandon.li.gn@gmail.com.

From the repository root:

```sh
python3 -m pip install -r requirements.txt
sh run_checks.sh
```

| Script | Check | Output |
|---|---|---|
| `exact_checks.py` | Legendre identities, quartic coefficient, sample negative minors | `EXACT_CHECKS.json` |
| `bernstein_certificate.py` | Four exact polynomial sign certificates covering `0 < x <= 2/3` | `BERNSTEIN_CERTIFICATE.json` |
| `positive_kernel_algebra.py` | Elliptic factorizations and derivative signs | `EXACT_ALGEBRA_CHECKS.json` |
| `direct_continuation_algebra.py` | Pullback singularities and expansion at infinity | `DIRECT_ALGEBRA_CHECKS.txt` |
| `positive_kernel_diagnostics.py` | High-precision dispersion comparisons | `POSITIVE_KERNEL_DIAGNOSTICS.json` |
| `full_circle_diagnostics.py` | 132 angular comparisons of the continued branches | `FULL_CIRCLE_DIAGNOSTICS.json` |
| `measure_moments.py` | Legendre moments against the positive spectral representation | `MEASURE_MOMENTS.json` |

The algebra and sign certificates use exact arithmetic; the other scripts
compare the formulas numerically at the listed parameters.

`independent_continuation.py` continues the elliptic germ by its
differential equation and compares the result with the boundary formulas
at the end:

```sh
python3 -m pip install -r requirements-optional.txt
python3 checks/independent_continuation.py
```

It writes `checks/independent_continuation.json`.
