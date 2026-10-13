<img src="logo.svg" width="50%" />

# Introduction to data science

This repository contains lecture materials for the "Introduction to data science" course at the [Data Science Master's program](https://datascience.fri.uni-lj.si) at the University of Ljubljana, Faculty for computer and information science.

Compiled version of the materials is accessible at [https://fri-datascience.github.io/course_ids](https://fri-datascience.github.io/course_ids).

Introductory lesson slides are available at [https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html](https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html).

The course is administered by professors [Erik Štrumbelj](mailto:erik.strumbelj@fri.uni-lj.si), [Tomaž Curk](mailto:tomaz.curk@fri.uni-lj.si) and [Slavko Žitnik](mailto:slavko.zitnik@fri.uni-lj.si)

## Repository updates

The repository was initially created and used during the Fall 2019 and is now being updated each year for the course. You are also invited to contribute to the repository.

### Building with Docker (preferred)

Build everything inside a Docker container, with no local R, Python or LaTeX installation needed. The included [Dockerfile](Dockerfile) provides R, all required packages, pandoc and TeX Live. The image is built automatically on first use.

```
./build.sh html    # HTML gitbook into docs/handbook/
./build.sh pdf     # docs/handbook/IDS-handbook.pdf
./build.sh all     # both (default)
./build.sh clean   # remove intermediate bookdown files
./build.sh shell   # interactive shell in the build container
./build.sh image   # rebuild the Docker image (e.g. after editing Dockerfile)
```

### Building with RStudio

Alternatively, to make updates we propose to use RStudio IDE and xelatex (using [TeX Live](https://tug.org/texlive/)). Prior to work on a project we advise to install the following dependencies:

```
install.packages(c("devtools", "remotes"))

remotes::install_github("slowkow/ggrepel")
install.packages(c("FactoMineR", "ggpubr"))
devtools::install_github("kassambara/factoextra")

install.packages(c("GPArotation", "bookdown", "reticulate", "moments", "ggcorrplot", "tmvnsim", "mnormt", "psych", "Rtsne", "naniar", "mice", "caret", "ggplot2", "gbm"))
```

After that build the *bookdown* project, the newly compiled materials will be available in folder */docs/handbook.* Use R commands as follows:

```
# Clean existing book data
bookdown::clean_book(TRUE)

# Clean R environment
rm(list = ls()) 

# Build HTML gitbook
bookdown::render_book('index.Rmd', 'bookdown::gitbook')

# Build PDF version
bookdown::render_book('index.Rmd', 'bookdown::tufte_book2')
```

--

<center><img src="cc_license.png"></center>

This work is published under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license (CC BY-NC-SA)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). Creative Commons licenses are built of four building blocks, each corresponding to a different requirement:

* BY (attribution): this is a mandatory element of every CC license. Contrary to what is commonly believed, the attribution obligation in CC licenses extends beyond a simple indication of the name of the author; in fact, the user is obliged to retain a copyright notice (e.g. "(c) 2016 Paweł Kamocki"), a license notice (e.g. "This work is licensed under a Creative Commons Attribution 4.0 International License"), a disclaimer of warranties (if supplied) and a link to the licensed material.
* NC (non-commercial) means that no commercial use can be made. Commercial use is defined as use primarily intended for commercial advantage or monetary compensation. Please note that this category is extremely unclear and can discourage potential users. In our view, when it comes to licensing of research data, this requirement should be avoided.
* SA (share-alike): according to this requirement, if derivative works are made, they have to be licensed under the same or compatible license, i.e. a license containing the same (or compatible) requirements. There is only one license approved for compatibility with CC BY-SA 4.0 license: the Free Art License 1.3. In every other case, in order to comply with the SA requirement, you will have to re-license the derivative work under the same CC license, or its more recent version.
