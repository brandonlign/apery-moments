#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p ../build
if command -v tectonic >/dev/null 2>&1; then
  tectonic -X compile manuscript.tex --outdir ../build
elif command -v pdflatex >/dev/null 2>&1; then
  for i in 1 2; do
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../build manuscript.tex
  done
else
  echo 'Install Tectonic or TeX Live (pdflatex) to rebuild the manuscript.' >&2
  exit 1
fi
