# ---- setup
library(tidyverse)
library(grid)
library(gridExtra)

figs <- function(key) {
  fig_dir <- file.path("img", key)
  return(function(stem, ...) {
    img(stem, img_dir = fig_dir, ...)
  })
}

img <- function(stem, img_dir = "img", ext = ".png", draw = FALSE) {
  if (ext == ".png") {
    image_reader <- png::readPNG
  } else if (ext == ".jpg") {
    image_reader <- jpeg::readJPEG
  } else {
    stop(paste("unknown image ext", ext))
  }
  
  if (file.exists(stem)) {
    img_path <- stem
  } else {
    img_path <- file.path(img_dir, paste0(stem, ext))
  }
  
  grob <- image_reader(img_path) %>%
    grid::rasterGrob()
  
  if (draw == TRUE) {
    grid::grid.newpage()
    grid::grid.draw(grob)
  } else {
    return(grob)
  }
}
