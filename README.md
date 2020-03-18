<img src="logo.svg" width="50%" />

# Introduction to data science

This repository contains lecture materials for the "Introduction to data science" course at the [Data Science Master's program](https://datascience.fri.uni-lj.si) at the University of Ljubljana, Faculty for computer and information science.

Compiled version of the materials is accessible at [https://fri-datascience.github.io/course_ids](https://fri-datascience.github.io/course_ids).

Introductory lesson slides are available at [https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html](https://fri-datascience.github.io/course_ids/slides/00-intro.slides.html).

## Repository updates

The repository was initially created and used during the Fall 2019 and is now being updated each year for the course. You are also invited to contribute to the repository.

To make updates we propose to use RStudio with the following dependencies:

```
install.packages(c("factoextra", "GPArotation", "bookdown", "reticulate", 
"moments", "ggcorrplot", "psych", "Rtsne", "naniar", "mice", "caret", 
"ggplot2", "gbm"))
```

After that build the *bookdown* project (using RStudio or provided *build.sh* script) and the newly compiled materials will be available in folder */docs/handbook.*
