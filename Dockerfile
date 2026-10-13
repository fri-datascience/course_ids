# Build environment for the "Introduction to data science" handbook.
# Renders the bookdown project to HTML (gitbook) and PDF; see build.sh.
FROM rocker/r-ver:4.5.1

ENV DEBIAN_FRONTEND=noninteractive \
    RETICULATE_PYTHON=/usr/bin/python3

# pandoc, TeX Live (with tlmgr) and system libraries needed by R packages
RUN /rocker_scripts/install_pandoc.sh \
 && /rocker_scripts/install_texlive.sh \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      python3 libpython3-dev \
      libxml2-dev libcurl4-openssl-dev libssl-dev \
      libfontconfig1-dev libfreetype6-dev libpng-dev libjpeg-dev \
      libharfbuzz-dev libfribidi-dev libtiff5-dev \
      cmake fonts-dejavu \
 && rm -rf /var/lib/apt/lists/*

ENV PATH=/usr/local/texlive/bin/linux:$PATH

# LaTeX packages used by bookdown::pdf_book
RUN tlmgr install \
      amsfonts amsmath bookmark booktabs caption etoolbox fancyvrb float \
      framed geometry hyperref iftex lm lm-math natbib oberdiek \
      parskip setspace tools unicode-math upquote url xcolor xurl \
      footnotehyper fvextra mdwtools ulem multirow wrapfig colortbl \
      pdflscape tabu varwidth threeparttable threeparttablex environ \
      makecell epstopdf-pkg grffile titling newunicodechar \
      babel-english hyphen-english cm-super ec inconsolata \
 && tlmgr path add

# R packages used in the book chapters
RUN install2.r --error --skipinstalled --ncpus -1 \
      bookdown rmarkdown knitr reticulate tinytex \
      ggplot2 ggrepel ggpubr reshape2 MASS cluster scatterplot3d \
      psych GPArotation moments ggcorrplot FactoMineR factoextra \
      Rtsne naniar UpSetR mice caret gbm \
 && rm -rf /tmp/downloaded_packages

WORKDIR /book
