
#!/bin/bash

rm log.txt

for i in $(seq -f "%02g" 1 12);
  do
    cd "src/Lecture$i"

    echo "Compiling Lecture $i"

    pdflatex "\PassOptionsToClass{handout}{beamer}\input{lecture.tex}" 
    pdflatex "\PassOptionsToClass{handout}{beamer}\input{lecture.tex}"
    mv lecture.pdf ../../handouts/handout$i.pdf

    pdflatex lecture.tex -o slides$i.pdf 
    pdflatex lecture.tex -o slides$i.pdf 
    mv lecture.pdf ../../slides/slides$i.pdf

    find . ! -name 'lecture.tex' -type f -exec rm -f {} +

    cd ../../
  done  

