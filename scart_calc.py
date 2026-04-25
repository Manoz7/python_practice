# Part 6: Validate extracted data

import re

# DO NOT MODIFY
cart_details = """
Apples - 2 pcs - $1.50 per pc - PRD-1001
Bananas - 4 pcs - $0.80 per pc - PRD-1234
Oranges - 6 pcs - $0.75 per pc - PRD-5678
"""

# Extract data (same as Part 5)
pattern = r'([A-Za-z]+)\s*-\s*(\d+)\s*pcs\s*-\s*\$(\d+\.\d+)\s*per pc\s*-\s*(PRD-\d{4})'
matches = re.findall(pattern, cart_details)

# Regex for product code validation
code_pattern = r'^PRD-\d{4}$'

# Validation
for match in matches:
    product, quantity, price, code = match

    quantity = int(quantity)
    price = float(price)

    # Quantity validation
    if quantity > 0:
        print(f"Valid quantity for {product}: {quantity}")
    else:
        print(f"Invalid quantity for {product}: {quantity}")

    # Price validation
    if price > 0:
        print(f"Valid price for {product}: {price}")
    else:
        print(f"Invalid price for {product}: {price}")

    # Product code validation (regex)
    if re.match(code_pattern, code):
        print(f"Valid product code: {code}")
    else:
        print(f"Invalid product code: {code}")


# Part 7: Print a formatted table
print(f"{'Product':<15}{'Quantity':<15}{'Unit Price ($)':<20}{'Total ($)':<15}{'Product Code'}")
print("=" * 81)

overall_total = 0
for product, product_quantity, price, code in matches:
  qty = int(product_quantity)
  price = float(price)

  total = qty * price
  overall_total += total

  print(f"{product:<15}{qty:<15}{price:<20.2f}{total:<15.2f}{code}")

print("=" * 81)

# Print Overall Total
print (f"{'Overall Total' :<49} ${overall_total:.2f}")

# Print Total after Discount
if overall_total > 100:
  discounted_total = overall_total * 0.9
else:
  discounted_total = overall_total

print(f"{'Total After Discount' :<50}${discounted_total:.2f}")