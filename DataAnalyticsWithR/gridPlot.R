library(ggplot2)
library(gridExtra)

set.seed(100)
num_students <- 10

students_data <- data.frame(
  names = paste("students",1:num_students),
  scores = sample(60:100,num_students,replace = TRUE),
  attendance = sample(60:80,num_students,replace = TRUE)
)

scatter_plot <- ggplot(students_data,aes(x=attendance,y=scores)) +
  geom_point(color = "red", size = 3) +
  labs(title = " SCATTER PLOT ", x= "x", y= "y") + 
  theme_bw()
print(scatter_plot)

bar_plot <- ggplot(students_data,aes(x=names,y=scores,fill = names)) +
  geom_bar(stat = "identity",color="lightblue") + 
  labs(title = "BAR PLOT", x="x2",y="y2") + theme_light()

print(bar_plot)
students_data$time <- 1:num_students

line_plot <- ggplot(students_data,aes(x=time,y=scores)) + 
  geom_line(stat = "identity", color = "purple") + 
  labs(title = "LINE PLOT",x="x3",y="y3") + theme_minimal()

histo_plot <- ggplot(students_data,aes(x=scores)) + 
  geom_histogram(binwidth = 5,fill="green",color="white") +
  labs(title = "HISTOGRAM PLOT",x="x4",y="y4") + theme_light()

grid.arrange(bar_plot,line_plot,scatter_plot,histo_plot,ncol=2)
