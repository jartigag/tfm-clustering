\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{formato/UNIR}[2018/09/01 UNIR TFM LaTeX class]

% Clase base (libro)
\LoadClass[a4paper,11pt,oneside]{book}
\RequirePackage{courier}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}


% Bibliografía (no establecido por UNIR, cosecha propia)
\usepackage[bibencoding=utf8,maxcitenames=1,backend=biber,bibstyle=authoryear,citestyle=apa,sorting=ynt]{biblatex}
\addbibresource[location=local]{contenido/TFM-biblio.bib}
%\AtEveryBibitem{[\printfield{labelnumber}]\addspace}
% \cite{xxx} -> (Author, Year)
\renewcommand*{\cite}[1]{\parencite{#1}}
% \apa{XXX} -> Author (Year)
\newcommand*{\apa}[1]{\citeauthor{#1} (\citeyear{#1})}


% Conveniencia: negrita con comando \n (para preservar identado de tablas con negrita)  
\def\n{\bfseries}
\def\glmtr{\guillemotright}
\def\glmtl{\guillemotleft}
% Gráficos
\RequirePackage{graphicx}

% Parámetros de entrada (aparte de title, author y date)
\RequirePackage{xstring}
\RequirePackage{etoolbox}

\def\autor#1{\author{#1}}
\def\titulo#1{\title{#1}}
\def\fecha#1{\date{#1}}
\def\universidad#1{\gdef\@universidad{#1}}
\def\escuela#1{\gdef\@escuela{#1}}
\def\master#1 {\gdef\@master{#1}}
\def\tipoTesis#1{\gdef\@tipoTesis{#1}}
\def\director#1{\gdef\@director{#1}}
\def\ciudad#1{\gdef\@ciudad{#1}}
\gdef\keywords#1{\gdef\keywordsv{#1}}
\gdef\keywordsEs#1{\gdef\keywordsESv{#1}}



%Tablas
\RequirePackage{float}
\RequirePackage{tabularx}
\newcolumntype{L}[1]{>{\hsize=#1\hsize\raggedright\arraybackslash}X}%
\newcolumntype{R}[1]{>{\hsize=#1\hsize\raggedleft\arraybackslash}X}%
\newcolumntype{C}[1]{>{\hsize=#1\hsize\centering\arraybackslash}X}%
\newcommand{\cc}[1]{\begin{minipage}[c][0.5cm][c]{0.5cm}\centering#1\end{minipage}}

%Captions de imágenes y tables con números consecutivos (no por capítulos)
\RequirePackage[font=small,skip=2pt]{caption}
\RequirePackage{subcaption}
\captionsetup{within=none}

% Formato de Código (no establecido por UNIR, cosecha propia)
\newenvironment{codigo}{
    \begin{minipage}[t][][t]{0.7\textwidth}
    \ttfamily \small \linespread{0}
}{
    \end{minipage}
}
\newcommand{\cod}{\ttfamily \small \linespread{0}}

%  Abstract/Resumen acorde a la UNIR
\newenvironment{abstract}[1][Abstract]{%
    \begin{center}%
        {\fontsize{14}{14}\selectfont\bfseries #1\vspace{-0.5em}}%
    \end{center}%
    \quotation
}{\endquotation\vspace{1cm}}

% Imágenes y texto en dos columnas
\RequirePackage{wrapfig}

%Código
\RequirePackage{multicol}
\RequirePackage{minted}
\newcommand{\Rprompt}{%
  \def\FancyVerbFormatLine##1{{\color{red}>}\ ##1}%
}
\setminted{breaklines,breakbytokenanywhere=true,frame=lines,fontsize=\footnotesize,baselinestretch=1}
%\setminted[R]{linenos,style=tango,formatcom=\Rprompt}
\setminted[text]{linenos=FALSE,formatcom=\color{azul}}
\newcommand{\out}[1]{\vspace*{-1.2\baselineskip}\inputminted{text}{#1}}
