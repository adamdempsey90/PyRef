#!/bin/bash


python3 PyRef.py $1 $2

#latexmk -cd -e -f -pdf -interaction=nonstopmode -synctex=1 "$2"
