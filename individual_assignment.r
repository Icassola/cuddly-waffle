#individual assignment
#Trying to read prepared venezuela_data.csv from python done
library(readr)
library(ggplot2)

venezdata <- venezuela_data

ggplot() + 
  geom_bar(data = venezdata, mapping = aes(x = year, colour = deaths_civilians))

