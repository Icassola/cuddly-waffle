#individual assignment
#Trying to read prepared venezuela_data.csv from python done
library(readr)
library(ggplot2)

venezdata <- read.csv('venezuela_data', stringsAsFactors=FALSE) 

events_per_year <- count(venezdata, year)
deaths_per_year <- count()

ggplot() + 
  geom_bar(data = venezdata, mapping = aes(x = year))


ggplot(data = venezdata) +
  geom_point(mapping = aes(x=year, y= deaths_civilians))

ggplot(data = venezdata) +
  geom_bar(mapping =aes(x=year, y=events_per_year) (stat= 'identity'))