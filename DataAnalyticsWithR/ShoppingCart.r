taxrate <- 0.08
shopping_cart <- list()
num <- as.integer(readline("Enter number of products: "))

for(i in 1 : num){
  name <- readline(paste("Enter product name :"))
  price <- as.integer(readline("Enter price :"))
  quantity <- as.integer(readline("Quantity :")) 
  
  shopping_cart[[i]] <- list("name"=name,"price"=price,"quantity"=quantity)
}
subtotal <- 0

cat( "- item \t price \t quantity \t total -")
for(item in shopping_cart){
  item_subT <- item$quantity * item$price
  subtotal <- subtotal + item_subT
  cat("\n","\t",item$name ,"\t", item$price , "\t" , item$price, "\t", item_subT)
}

tax <- taxrate * subtotal
finalprice <- subtotal + tax

cat("\nSubtotal: ", subtotal)
cat("\nTax (8%): ", tax)
cat("\nFinal Total: ", finalprice)
cat("\n--- Thank You! ---\n")
