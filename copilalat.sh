#!/bin/bash

rm $1.pdf

pdflatex $1".tex"

rm $1.aux
rm $1.log
rm $1.nav
rm $1.out
rm $1.snm
rm $1.toc

open $1.pdf

