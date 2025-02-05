# Load necessary library
library(dplyr)

# Create an empty data frame to store student information
student_data <- data.frame(
  Name = character(0),
  Math_Score = numeric(0),
  Science_Score = numeric(0),
  History_Score = numeric(0),
  Attendance = numeric(0),
  stringsAsFactors = FALSE
)

# 📌 Function to Add a New Student
add_student <- function() {
  name <- readline("Enter student name: ")
  math_score <- as.numeric(readline("Enter Math score: "))
  science_score <- as.numeric(readline("Enter Science score: "))
  history_score <- as.numeric(readline("Enter History score: "))
  attendance <- as.numeric(readline("Enter Attendance percentage: "))

  # Add new student to data frame
  new_student <- data.frame(Name = name,
                            Math_Score = math_score,
                            Science_Score = science_score,
                            History_Score = history_score,
                            Attendance = attendance,
                            stringsAsFactors = FALSE)

  # Append to the global student data frame
  student_data <<- bind_rows(student_data, new_student)

  cat("✅ Student added successfully!\n")
}

# 📌 Function to Generate a Performance Report
generate_report <- function() {
  if (nrow(student_data) == 0) {
    cat("⚠ No student data available to generate a report.\n")
    return()
  }

  # Calculate Average Scores
  student_data$Average_Score <- round((student_data$Math_Score +
                                        student_data$Science_Score +
                                        student_data$History_Score) / 3, 2)

  # Assign Attendance Status
  student_data$Attendance_Status <- ifelse(student_data$Attendance < 70, "Low", "Good")

  # Select relevant columns for report
  report <- student_data[, c("Name", "Average_Score", "Attendance", "Attendance_Status")]

  # Print Report
  cat("\n--- 📊 Student Performance Report ---\n")
  print(report)
}

# 📌 Main Program Loop
while (TRUE) {
  cat("\n📌 Menu:\n1️⃣ Add Student\n2️⃣ Generate Report\n3️⃣ Exit\n")
  choice <- as.integer(readline("Enter your choice: "))

  if (choice == 1) {
    add_student()
  } else if (choice == 2) {
    generate_report()
  } else if (choice == 3) {
    cat("👋 Exiting the program. Goodbye!\n")
    break
  } else {
    cat("⚠ Invalid choice. Please try again.\n")
  }
}
