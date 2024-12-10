fine_per_day <- 7
fine_cap <- 50

calculate_fine <- function(days){
  
  if(days < 3){
    fine <- 0
  }else if(days >= 30){
    fine <- fine_cap
  }else{
    fine <- fine_per_day * days
  }
  
  return(fine)
}

days = as.numeric(readline(paste(" Enter the number of days overdue :")))

fine = calculate_fine(days)
if(fine == 0){
  cat("fine = 0, Return the book soon")
} else if(fine == fine_cap){
  cat("Max fine reached, Return ASAP, fine = ", fine)
} else{
  cat("fine = ",fine, " Return the book ASAP")
}
