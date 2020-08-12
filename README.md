<img src="logo.svg" width="50%" />

# Introduction to data science

This repository contains lecture materials for the "Introduction to data science" course at the [Data Science Master's program](https://datascience.fri.uni-lj.si) at the University of Ljubljana, Faculty for computer and information science.

Compiled version of the materials is accessible at [https://fri-datascience.github.io/course_ids](https://fri-datascience.github.io/course_ids).

Introductory lesson slides are available at [https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html](https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html).

The course is administered by professors [Erik Štrumbelj](mailto:erik.strumbelj@fri.uni-lj.si), [Tomaž Curk](mailto:tomaz.curk@fri.uni-lj.si) and [Slavko Žitnik](mailto:slavko.zitnik@fri.uni-lj.si)

## Repository updates

The repository was initially created and used during the Fall 2019 and is now being updated each year for the course. You are also invited to contribute to the repository.

To make updates we propose to use RStudio IDE. Prior to work on a project we advise to install the following dependencies:

```
install.packages(c("factoextra", "GPArotation", "bookdown", "reticulate", 
"moments", "ggcorrplot", "tmvnsim", "mnormt", "psych", "Rtsne", "naniar", "mice", "caret", 
"ggplot2", "gbm"), repos="https://cran.wu.ac.at/")
```

After that build the *bookdown* project, the newly compiled materials will be available in folder */docs/handbook.* Use R commands as follows:

```
# Clean existing book data
bookdown::clean_book(TRUE)

# Build HTML gitbook
bookdown::render_book('index.Rmd', 'bookdown::gitbook', clean_envir = TRUE)
```
