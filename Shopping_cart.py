# Part 1: Adding Items to the Cart

# Ask the user how many items they want to add to the cart
num_items = int(input("Enter the number of items you want to add to the cart: \n"))
# Initialize an empty list to store the items
items = []
# For each item, ask for the name, price, and quantity
for no in range(num_items):
  item_name = input(f"Enter the name of item {no+1}: \n")
  item_cost = float(input(f"Enter the price of {item_name}: \n"))
  item_no = int(input(f"Enter the quantity of {item_name}: \n"))

  items.append({
      "item_name": item_name,
      "item_cost": item_cost,
      "item_no" : item_no
  })

# Output the items and their total cost
print("Items in your cart: ")
for item in items:
  item_total = item["item_cost"] * item["item_no"]
  print(f"{item["item_no"]} x {item["item_name"]} @ ${item["item_cost"]} each = ${item_total:.2f}")

  # Part 2: Calculate the Total Cost

# Initialize a variable to store the total cost
total_cost_cart = 0
# Output the total cost
for item in items:
  item_total = item['item_cost'] * item['item_no']
  total_cost_cart += item_total

print(f"Total cost of your cart: ${total_cost_cart:.2f}")

# Part 3: Apply Discount

# Check if a discount applies
if total_cost_cart > 100:
  print("10% discount has been applied!")
  
  print(f"Total cost before discount: ${total_cost_cart:.2f}")
  total_cost_cart_after_discount = total_cost_cart * 0.9
  print(f"Discounted total: ${total_cost_cart_after_discount:.2f}")

else:
  print("No discount applied.")

  # Part 4: Option to Add More Items

# Repeat the process of adding items
while True:
  choice = input("Do you want to add more items to your cart? (yes/no) \n")

  if choice == "yes":
    num_items = int(input("Enter the number of items you want to add: \n"))

    for no in range(num_items):
      print()
      item_name = input(f"Enter the name of item {no+1}: \n")
      item_cost = float(input(f"Enter the price of {item_name}: \n"))
      item_no = int(input(f"Enter the quantity of {item_name}: \n"))

      item_total = item_cost * item_no
      total_cost_cart += item_total

      items.append({
          "item_name": item_name,
          "item_cost": item_cost,
          "item_no" : item_no
      })
    print(f"\nUpdated total cost : ${total_cost_cart:.2f} \n")

   # Break out of the loop if user doesn't want to add more items
  elif choice == "no":
    break

  else:
    print("Please enter yes or no.")


# Apply discount logic again after the update
if total_cost_cart > 100:
  print("10% discount has been applied!")

  print(f"Total cost before discount: ${total_cost_cart:.2f}")
  total_cost_cart_after_discount = total_cost_cart * 0.9
  print(f"Discounted total: ${total_cost_cart_after_discount:.2f}")

else:
  print("\nNo discount applied.")