install.packages("gratis")
devtools::install_github("ykang/gratis")
library(gratis)
library(feasts)
set.seed(1)
mar_model(seasonal_periods=12) %>%
  generate(length=120, nseries=2) %>%
  autoplot(value)