# Task 1: Matrix Creation
matrix_A <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, ncol = 3, byrow = TRUE)
matrix_B <- matrix(c(9, 8, 7, 6, 5, 4, 3, 2, 1), nrow = 3, ncol = 3, byrow = TRUE)

# Task 2: Matrix Manipulation
sum_matrix <- matrix_A + matrix_B
scaled_matrix <- matrix_A * 2

# Task 3: Matrix Operations
transposed_A <- t(matrix_A)
product_matrix <- matrix_A %*% matrix_B

# Task 4: Matrix Statistics
sum_matrix_A <- sum(matrix_A)
mean_matrix_B <- mean(matrix_B)
sd_matrix_B <- sd(matrix_B)

# Task 5: Visualizationlibrary(ggplot2)
library(reshape2)

# Melt Matrix A for Heatmap
melted_data <- melt(matrix_A)

# Create Heatmap
heatmap_data <- ggplot(melted_data, aes(x=Var2, y=Var1, fill=value)) +  # Fix x and y axes
  geom_tile() +
  scale_fill_gradient(low="white", high="red") +  # Better contrast
  labs(title="Heatmap of Matrix A", x="Columns", y="Rows")

# Compute Row Sums for Matrix B
row_sums <- rowSums(matrix_B)
row_names <- paste("Row", 1:3)  # Fix row names format

# Create Data Frame for Bar Plot
row_data <- data.frame(Row = row_names, Sums = row_sums)

# Create Bar Plot
barplot_data <- ggplot(row_data, aes(x=Row, y=Sums, fill=Row)) +  # Fix axes
  geom_bar(stat="identity", color="black") +  # Border color
  ggtitle("Row Sum Comparison of Matrix B") +
  xlab("Row Index") +
  ylab("Row Sum") +
  theme_minimal()

# Print Plots
print(heatmap_data)  # Displays heatmap
print(barplot_data)  # Displays bar plot
