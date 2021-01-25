#!/bin/sh

latexmk -pdf --shell-escape TFM.tex
# creo que `pdflatex --shell-escape TFM.tex` es más rápido, pero Overleaf usa latexmk

# recoger ficheros auxiliares en .tmp/ :
mkdir -p .tmp/contenido/
mkdir -p .tmp/_minted-TFM/
find . -maxdepth 1 -name 'TFM*' ! -name 'TFM.tex' ! -name 'TFM.pdf' -type f -exec mv {} .tmp/ \;
mv contenido/*.aux .tmp/contenido/
mv -f _minted-TFM/* .tmp/_minted-TFM/
rm -r _minted-TFM/
