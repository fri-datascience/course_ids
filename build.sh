#!/bin/sh

clear
echo
echo "ZAČETEK gradnje knjige"
echo

rm -rf _target/*
Rscript -e "bookdown::clean_book(TRUE)"
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

echo
echo "KONEC gradnje knjige"
echo
