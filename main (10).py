total_extended_price = 0
order_count = 0
extended_prices = []

# Open the data file for reading
with open("example_data.txt", "r") as file:
    lines = file.read().splitlines()

# Iterate through the lines in the file
for i in range(0, len(lines), 3):
    item = lines[i]
    quantity = int(lines[i + 1])
    price = float(lines[i + 2])

    extended_price = quantity * price
    total_extended_price += extended_price
    order_count += 1
    extended_prices.append(extended_price)

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Extended Price:", extended_price)
    print()

# Calculate the average order
if order_count > 0:
    average_order = total_extended_price / order_count
else:
    average_order = 0

# Display the sum of all extended prices, count of orders, and average order
print("Sum of all Extended Prices:", total_extended_price)
print("Number of Orders:", order_count)
print("Average Order:", average_order)