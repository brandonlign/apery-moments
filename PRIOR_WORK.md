# Prior-work and novelty assessment (22 November 2026)

## Paper at issue

Brandon Li and Ethan Yeroushalmi, *Stieltjes moment classification of Apéry polynomials* (this repository). The central mathematical classification stated by the manuscript is

```text
(A_n(x))_{n>=0} is a Stieltjes moment sequence, for real x>=0,
if and only if x=0 or x>=1.
```

The classification statement is unchanged by the priority correction. What changes is the attribution of the two directions and the novelty claim.

## Earlier sources and dates

1. G. A. Edgar, *The Apéry Numbers as a Stieltjes Moment Sequence*, arXiv:2005.10733 (2020; underlying 2017 manuscript): establishes the special case `x=1`.
   https://arxiv.org/abs/2005.10733

2. Knowledge Sense, *Apéry polynomials as Stieltjes moment sequences*, dated **13 October 2026**, first publicly committed to `KnowledgeSense/math` on **14 October 2026**:
   https://github.com/KnowledgeSense/math/tree/main/preprints/Apery-Polynomials-as-Stieltjes-Moment-Sequences-October-13-2026

   Public commit documenting the deposit:
   https://github.com/KnowledgeSense/math/commit/91f1bdd2a10abeb28acc742ce3ee884874caf124

   The earlier manuscript's main theorem establishes **all real x>=1**, constructing a positive, compactly supported density and giving its explicit formula. Its introduction expressly says that the conjectured negative case **0<x<1 is not addressed**.

3. The initial commit of this repository, **8 November 2026**, postdates the Knowledge Sense preprint:
   https://github.com/brandonlign/apery-moments/commit/0802ad3508bb2dc65f5f1b9faba400559220e149

A repository timestamp shows the public availability of a manuscript; by itself it does not certify independent proof correctness or rule out earlier unpublished results.

## Theorem-by-theorem scope

| Statement in this repository | Proper attribution and status |
| --- | --- |
| Positivity / existence of a Stieltjes measure for `x=1` | Previously proved by Edgar |
| Positivity / existence for **every `x>=1`** | Previously proved by Knowledge Sense; the proof here is an *alternative derivation*, not a first solution |
| Failure of the Stieltjes property for **`0<x<1`** | Not treated in the identified Knowledge Sense manuscript; this is the *primary new result claimed by our manuscript*, subject to broader priority and proof review |
| `x=0` | Trivial: `A_n(0)=1`, represented by a point mass at 1 |
| Full classification on `x>=0` | Obtained by combining our claimed negative-range theorem with previously known positivity (and `x=0`), rather than independently resolving both sides for the first time |
| Explicit rational Hankel-minor obstructions for `0<x<=2/3` | Supporting result of this manuscript; independent novelty versus all literature has not been established |
| Alternative elliptic-integral representation for `x>1` | May be methodologically distinct, but the existence theorem itself was already known |

## Editorial implications

- The abstract and introduction should identify the **negative parameter interval** as the principal novelty and cite the **October 2026 Knowledge Sense preprint** prominently.
- Do not describe the `x>=1` result as still open or claim this manuscript is its first proof.
- It remains accurate to present a full classification, provided prior positive-range results are clearly credited.
- Do not claim that the different proof method, exact Hankel certificates, or the negative-range result have independently certified priority without a comprehensive literature check.
- The checked-in `manuscript.pdf` predates the wording corrections to `source/manuscript.tex` and `source/positive_section.tex`. **Regenerate the PDF before circulating the revised paper.**
- The repository edits do not automatically revise an existing Zenodo record or deposited PDF. Correct these separately if applicable.

## Verification scope

This note compares the theorem statements and the publicly available LaTeX manuscript of the Knowledge Sense preprint with the source of this repository. It does **not** verify either manuscript's analytic proofs, independently reproduce all numerical checks, or certify originality against every other prior publication.
