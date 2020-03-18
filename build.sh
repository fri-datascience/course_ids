#!/bin/sh

clear
echo
echo "Building script ..."
echo

rm -rf docs/handbook/*
Rscript -e "bookdown::clean_book(TRUE)"
Rscript -e "bookdown::render_book('00-Index.Rmd', 'bookdown::gitbook')"

echo
echo "... script successfully built!"
echo
