# ---- setup
library(tidyverse)
library(grid)
library(gridExtra)

img <- function(stem) {
    file.path("img", paste0(stem, ".png")) %>%
        png::readPNG() %>%
        grid::rasterGrob()
}

