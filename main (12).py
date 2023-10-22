# Define a function to calculate the total with a 10% discount if it's over $10,000.
def calculate_total(quantity, price):
    total = quantity * price
    if total > 10000.00:
        total -= total * 0.10  # Apply a 10% discount
    return total

# Initialize variables to keep track of the sum and display the extended price.
total_sum = 0.0

# Continue taking user input until Ctrl+Z is pressed.
try:
    while True:
        # Ask the user for quantity and price.
        quantity = float(input("Enter quantity: "))
        price = float(input("Enter price: "))

        # Calculate the total and add it to the sum.
        total = calculate_total(quantity, price)
        total_sum += total

        # Display quantity, price, and total.
        print(f"Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")

except EOFError:
    pass  # Ctrl+Z pressed, exit the loop

# Display the sum of extended prices.
print(f"Sum of Extended Prices: ${total_sum:.2f}")