num_students <- 5
num_courses <- 3

# Function to assign grades
assign_grade <- function(average) {
  if (average >= 90) {
    return("A")
  } else if (average >= 80) {
    return("B")
  } else if (average >= 70) {
    return("C")
  } else {
    return("D")
  }
}

# List to store student data
students <- list()

# Input data for each student
for (i in 1:num_students) {
  name <- readline(paste("Enter name of student", i, ": "))
  marks <- numeric(num_courses)
  sumM <- 0
  
  for (j in 1:num_courses) {
    marks[j] <- as.numeric(readline(paste("Enter marks for subject", j, ": ")))
    sumM <- sumM + marks[j]
  }
  
  avg_marks <- sumM / num_courses
  grade <- assign_grade(avg_marks)
  
  students[[i]] <- list(
    "name" = name,
    "marks" = marks,
    "total" = sumM,
    "average" = avg_marks,
    "grade" = grade
  )
}

# Output results
cat("\nStudent Performance:\n")
for (student in students) {
  cat("\nName: ", student$name, "\n")
  cat("Marks: ", paste(student$marks, collapse = ", "), "\n")
  cat("Total: ", student$total, "\n")
  cat("Average: ", student$average, "\n")
  cat("Grade: ", student$grade, "\n")
}
