inventory_items <- c()
inventory_quan <- c()

add_item <- function(item, quan) {
  inventory_items <<- c(inventory_items, item)  # Use <<- to update global variables
  inventory_quan <<- c(inventory_quan, quan)
  cat("Item", item, "x", quan, "added successfully!\n")
}

update_quan <- function(index, quan) {
  inventory_quan[index] <<- quan  # Update the quantity
  cat("Quantity updated successfully!\n")
}

display_inventory <- function() {
  if (length(inventory_items) == 0) {
    cat("-- INVENTORY EMPTY --\n")
  } else {
    cat("\n--- Current Inventory ---\n")
    for (i in seq_along(inventory_items)) {
      cat(i, "- Item:", inventory_items[i], "| Quantity:", inventory_quan[i], "\n")
    }
    cat("-------------------------\n")
  }
}

# Main Program
while (TRUE) {
  cat("\n--- Inventory Management System ---\n")
  cat("1. Add Item\n")
  cat("2. Update Quantity\n")
  cat("3. Display Inventory\n")
  cat("4. Exit\n")
  choice <- as.numeric(readline("Enter your choice: "))
  
  switch(choice,
         # Case 1: Add Item
         {
           item <- readline("Enter item name: ")
           quantity <- as.numeric(readline("Enter quantity: "))
           add_item(item, quantity)
         },
         # Case 2: Update Quantity
         {
           display_inventory()
           index <- as.numeric(readline("Enter item number to update: "))
           if (index > 0 && index <= length(inventory_items)) {
             quantity <- as.numeric(readline("Enter new quantity: "))
             update_quan(index, quantity)
           } else {
             cat("Invalid item number!\n")
           }
         },
         # Case 3: Display Inventory
         {
           display_inventory()
         },
         # Case 4: Exit
         {
           cat("Exiting the program. Goodbye!\n")
           break
         },
         # Default Case
         {
           cat("Invalid choice! Please try again.\n")
         })
}
