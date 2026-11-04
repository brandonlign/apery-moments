# Stieltjes moment classification of Apéry polynomials

Brandon Li

Paper and verification code for the Apéry polynomials

$$
A_n(x)=\sum_{k=0}^n\binom nk^2\binom{n+k}k^2x^k.
$$

For real $x\ge0$, $(A_n(x))_{n\ge0}$ is a Stieltjes moment sequence
exactly when $x=0$ or $x\ge1$.

- [Paper (PDF)](manuscript.pdf)
- [LaTeX source](source/)
- [Verification code](checks/)

## Reproduce

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python sh run_checks.sh
sh source/build.sh
```

The PDF builds with Tectonic, or with `pdflatex` and `bibtex`.

## License

Code: MIT. Paper and data: CC BY 4.0.
