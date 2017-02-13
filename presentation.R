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
  
  if (file.exists(stem)) {
    img_path <- stem
  } else {
    img_path <- file.path("img", paste0(stem, ext))
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

