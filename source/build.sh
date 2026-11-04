#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p ../build
if command -v tectonic >/dev/null 2>&1; then
  tectonic -X compile manuscript.tex --outdir ../build
elif command -v pdflatex >/dev/null 2>&1 && command -v bibtex >/dev/null 2>&1; then
  run() { pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../build manuscript.tex; }
  run
  (cd ../build && BIBINPUTS=../source: BSTINPUTS=../source: bibtex manuscript)
  run
  run
else
  echo 'Install Tectonic, or TeX Live (pdflatex and bibtex), to rebuild the manuscript.' >&2
  exit 1
fi
