# Run by bookdown before each chapter (see before_chapter_script in _bookdown.yml).

# Reseed before every chunk so figures are reproducible across builds
# and independent of chunks added or removed earlier in a chapter.
knitr::knit_hooks$set(reseed = function(before, options) if (before) set.seed(2025))
knitr::opts_chunk$set(reseed = TRUE)

# Tufte PDF: wide plots (fig.width >= 6 in) span text + margin; narrower plots
# stay in the text column with the caption in the margin. (fig.fullwidth is
# ignored by the HTML gitbook.)
knitr::opts_hooks$set(fig.width = function(options) {
  if (options$fig.width >= 6 && is.null(options$fig.fullwidth)) options$fig.fullwidth <- TRUE
  options
})

# Code/output blocks span the full page width in the PDF, so print R output
# at 80 characters instead of tufte's narrow-column default of 45.
knitr::knit_hooks$set(rwidth = function(before, options) if (before) options(width = 80))
knitr::opts_chunk$set(rwidth = TRUE)
