# Stieltjes moment classification of Apéry polynomials

Brandon Li and Ethan Yeroushalmi

Paper, source, and verification code for the Apéry polynomials

$$
A_n(x)=\sum_{k=0}^n\binom nk^2\binom{n+k}k^2x^k.
$$

## Result and prior-work correction

The manuscript establishes the classification that, for real $x\ge0$, $(A_n(x))_{n\ge0}$ is a Stieltjes moment sequence if and only if $x=0$ or $x\ge1$.

**Priority qualification (22 November 2026):** The positive-range statement for **every $x\ge1$ was already proved** by Knowledge Sense, *[Apéry polynomials as Stieltjes moment sequences](https://github.com/KnowledgeSense/math/tree/main/preprints/Apery-Polynomials-as-Stieltjes-Moment-Sequences-October-13-2026)*, dated 13 October 2026 and [committed publicly on 14 October 2026](https://github.com/KnowledgeSense/math/commit/91f1bdd2a10abeb28acc742ce3ee884874caf124). That work gives an explicit positive, compactly supported representing density. Edgar had earlier proved the special case $x=1$.

**The distinct contribution claimed here is the non-Stieltjes result for $0<x<1$**, which the Knowledge Sense manuscript explicitly leaves open. Together with the earlier positive-range theorem and the trivial $x=0$ case, this completes the classification for $x\ge0$. Our manuscript also gives an independent elliptic-integral proof of the already-established positive-range theorem and exact rational Hankel-minor certificates for $0<x\le2/3$. Those are not claimed as first proofs of positivity for $x\ge1$.

This priority comparison establishes overlap with the cited October preprint; it is not an exhaustive literature-priority certification or independent proof validation. See [PRIOR_WORK.md](PRIOR_WORK.md) for the scope comparison and sources.

## Files

- [Paper (PDF)](manuscript.pdf) — **older build; still contains the superseded priority wording in its abstract and introduction**
- [Revised LaTeX source](source/) — corrected credit and claims; build this for an updated PDF
- [Verification code](checks/)
- [Prior-work assessment](PRIOR_WORK.md)

## Reproduce

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python sh run_checks.sh
sh source/build.sh
cp build/manuscript.pdf manuscript.pdf  # replace the tracked PDF locally
```

The PDF builds with Tectonic or `pdflatex`. The checked-in `manuscript.pdf` is not yet regenerated; after running these commands, review the PDF and commit the refreshed binary before circulating it as a revised manuscript.

## License

Code: MIT. Paper and data: CC BY 4.0.
