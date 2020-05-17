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

# estos ficheros auxiliares son:

# latexmkrc  # VARiables de ENTORNO

# TFM.aux    # INFO de una compilación a otra (ej: refs. cruzadas):
             # \relax
             # \providecommand ....
             # \@input{contenido/....}
             # \xdef\lastpage@lastpage{7}
             # \xdef\lastpage@lastpageHy{14}

# TFM.lof    # FIGURAS:
             # \contentsline {figure}{\numberline {1}{ .... {figure.caption.10}%

# TFM.log    # LOG de la compilación (>1k líneas):
             # This is pdfTeX, Version 3.14159265-2.6-1.40.19 (TeX Live 2019/dev/Debian) (preloaded format=pdflatex 2020.5.13)

# TFM.lot    # CUADROS

# TFM.out    # hyperref lo genera para ENLACES dentro del pdf:
             # \BOOKMARK [0][-]{chapter.5} ....
             # \BOOKMARK [1][-]{section.9}{Objetivos}{chapter.5}% 2

# TFM.pdf    # fichero de SALIDA

# TFM.tex    # fichero de ENTRADA

# TFM.toc    # cabeceras de sección:
             # \babel@toc ....
             # \contentsline {chapter} ....
             # \contentsline {section} ....

# https://ondahostil.wordpress.com/2016/11/17/lo-que-he-aprendido-archivos-auxiliares-de-latex/
