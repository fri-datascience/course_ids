#!/usr/bin/env bash
# Build the handbook (HTML and/or PDF) inside a Docker container.
#
# Usage: ./build.sh [html|pdf|all|image|shell|clean]
#   html   build the HTML gitbook into docs/handbook/
#   pdf    build docs/handbook/IDS-handbook.pdf
#   all    build both (default)
#   image  (re)build the Docker image only
#   shell  open a bash shell in the build container
#   clean  remove intermediate bookdown files
set -euo pipefail

IMAGE="${IMAGE:-course-ids-build}"
TARGET="${1:-all}"
cd "$(dirname "$0")"

build_image() {
  docker build -t "$IMAGE" .
}

run() {
  docker image inspect "$IMAGE" >/dev/null 2>&1 || build_image
  docker run --rm -i $([ -t 0 ] && echo -t) \
    --user "$(id -u):$(id -g)" -e HOME=/tmp \
    -v "$PWD":/book -w /book \
    "$IMAGE" "$@"
}

render() {
  run Rscript -e "bookdown::render_book('index.Rmd', '$1')"
}

case "$TARGET" in
  html)  render bookdown::gitbook ;;
  pdf)   render bookdown::tufte_book2 ;;
  all)   render bookdown::gitbook; render bookdown::tufte_book2 ;;
  image) build_image ;;
  shell) run bash ;;
  clean) run Rscript -e "bookdown::clean_book(TRUE)" ;;
  *)     sed -n '2,10p' "$0"; exit 1 ;;
esac
