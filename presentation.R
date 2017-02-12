# ---- setup
library(tidyverse)
library(grid)
library(gridExtra)

img <- function(stem, ext = ".png", draw = FALSE) {
  if (ext == ".png") {
    image_reader <- png::readPNG
  } else if (ext == ".jpg") {
    image_reader <- jpeg::readJPEG
  } else {
    stop(paste("unknown image ext", ext))
  }
  
  grob <- file.path("img", paste0(stem, ext)) %>%
    image_reader() %>%
    grid::rasterGrob()
  
  if (draw == TRUE) {
    grid::grid.newpage()
    grid::grid.draw(grob)
  } else {
    return(grob)
  }
}

