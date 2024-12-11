library(forecast)

sales_data <- data.frame(
  months = seq(as.Date("2023-01-01"), as.Date("2023-06-01"), by = "months"),
  Sales = c(12000,15000,18000,16000,20000,22000)
)

sales_ts = ts(sales_data$Sales, frequency = 12, start = c(2023,1))
print(sales_ts)

arima_model= auto.arima(sales_ts)

forecastR <- forecast(arima_model, h = 6)

print(forecastR)
plot(forecastR)
