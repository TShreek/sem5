library(ggplot2)
library(gridExtra)

# Generate random data
set.seed(123)
num_students <- 15
students <- data.frame(
  Name = paste("Student", 1:num_students),
  Scores = sample(60:100, num_students, replace = TRUE),
  Attendance = sample(60:100, num_students, replace = TRUE)
)

# Scatter Plot: Scores vs Attendance
scatter_plot <- ggplot(students, aes(x = Scores, y = Attendance)) +
  geom_point(color = "red") +
  labs(
    title = "Scatter Plot - Scores vs Attendance",
    x = "Scores",
    y = "Attendance"
  )

# Bar Plot: Distribution of Scores
bar_plot <- ggplot(students, aes(x = Name, y = Scores)) +
  geom_bar(stat = "identity", fill = "orange") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(
    title = "Bar Plot - Distribution of Scores",
    x = "Student Names",
    y = "Scores"
  )

# Line Plot: Trend of Scores Over Time
students$Time <- seq_len(num_students)
line_plot <- ggplot(students, aes(x = Time, y = Scores, group = 1)) +
  geom_line(color = "purple") +
  labs(
    title = "Line Plot - Trend of Scores Over Time",
    x = "Time",
    y = "Scores"
  )

# Histogram: Distribution of Scores
histogram_plot <- ggplot(students, aes(x = Scores)) +
  geom_histogram(binwidth = 10, position = "identity", color = "brown") +
  scale_fill_brewer(palette = "Set3") +
  labs(
    title = "Distribution of Scores",
    x = "Scores",
    y = "Frequency"
  )

# Display the histogram individually
print(histogram_plot)

# Arrange all plots in a grid
grid.arrange(scatter_plot, bar_plot, line_plot, histogram_plot, ncol = 2)
