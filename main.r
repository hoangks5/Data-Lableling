library(gratis)
library(feasts)
set.seed(1)
mar_model(seasonal_periods=12) %>%
  generate(length=120, nseries=2) %>%
  autoplot(value)

mar_model(seasonal_periods=c(24, 24*7)) %>%
  generate(length=24*7*10, nseries=12) %>%
  autoplot(value)


  