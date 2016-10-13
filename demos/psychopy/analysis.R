# devtools::install_github("lupyanlab/property-verification", subdir = "propertyverificationdata")
library(propertyverificationdata)
data("question_first")

library(dplyr)
library(ggplot2)

question_first %<>%
  tidy_property_verification_data %>%
  recode_property_verification_data %>%
  label_outliers %>%
  filter(is_subj_outlier == 0, is_prop_outlier == 0)

ggplot(question_first, aes(mask_f, is_error)) +
  geom_bar(aes(fill = feat_type, alpha = mask_f, width = 1.0),
           stat = "summary", fun.y = "mean") +
  facet_wrap("feat_label") +
  scale_x_discrete("", labels = c("Blank screen", "Visual interference")) +
  scale_y_continuous("Error rate", labels = scales::percent) +
  scale_fill_manual(values = RColorBrewer::brewer.pal(3, "Set2")[c(1, 3)]) +
  scale_alpha_manual(values = c(0.6, 0.9)) +
  theme_minimal() +
  theme(legend.position = "none")
