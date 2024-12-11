# Load necessary library
library(dplyr)

# Create a data frame to store student information
student_data <- data.frame(
  Name = character(0),
  Math_Score = numeric(0),
  Science_Score = numeric(0),
  History_Score = numeric(0),
  Attendance = numeric(0)
)

# Function to add student information
add_student <- function() {
  name <- readline("Enter student name: ")
  math_score <- as.numeric(readline("Enter Math score: "))
  science_score <- as.numeric(readline("Enter Science score: "))
  history_score <- as.numeric(readline("Enter History score: "))
  attendance <- as.numeric(readline("Enter Attendance percentage: "))
  
  # Add the new student to the data frame
  new_student <- data.frame(
    Name = name,
    Math_Score = math_score,
    Science_Score = science_score,
    History_Score = history_score,
    Attendance = attendance
  )
  student_data <<- bind_rows(student_data, new_student)
  cat("Student added successfully!\n")
}

# Function to generate a performance report
generate_report <- function() {
  if (nrow(student_data) == 0) {
    cat("No student data available to generate a report.\n")
    return()
  }
  
  # Calculate average scores and attendance status
  report <- student_data %>%
    mutate(
      Average_Score = round((Math_Score + Science_Score + History_Score) / 3, 2),
      Attendance_Status = ifelse(Attendance < 70, "Low", "Good")
    ) %>%
    select(Name, Average_Score, Attendance, Attendance_Status)
  
  cat("\n--- Student Performance Report ---\n")
  print(report)
}

# Main program
while (TRUE) {
  cat("\n1. Add Student\n2. Generate Report\n3. Exit\n")
  choice <- as.integer(readline("Enter your choice: "))
  
  if (choice == 1) {
    add_student()
  } else if (choice == 2) {
    generate_report()
  } else if (choice == 3) {
    cat("Exiting the program. Goodbye!\n")
    break
  } else {
    cat("Invalid choice. Please try again.\n")
  }
}
