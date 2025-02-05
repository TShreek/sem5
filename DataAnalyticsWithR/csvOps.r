library(readr)
library(dplyr)
library(ggplot2)

set.seed(100)
customer_ids <- 1:100
purchase_amt <- sample(10000:22000,100,replace = TRUE)
csv_data <- data.frame(
  ids = customer_ids,
  amts = purchase_amt
)

write_csv(csv_data,"customer_data.csv")

purchase_data <- read.csv("customer_data.csv")
print(nrow(purchase_data))
print(n_distinct(purchase_data$amts))
print(mean(purchase_data$amts))
print(median(purchase_data$amts))
print(sd(purchase_data$amts))

print(
ggplot(purchase_data,aes(x=amts)) +
  geom_histogram(binwidth = 1000,color="green") +
  labs(title = "SALES HIST ") + theme_light()
)
