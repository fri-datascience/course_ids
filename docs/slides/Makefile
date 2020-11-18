SHELL := /bin/bash

NOTEBOOKS = $(wildcard [0-9][0-9]-*.ipynb)
NOTEBOOKS_html = $(foreach I,$(NOTEBOOKS),$(basename $I).slides.html)

%.slides.html: %.ipynb
	jupyter nbconvert $^ --to slides

all: $(NOTEBOOKS_html)

clean:
	rm -v [0-9][0-9]-*.slides.html
