# Function to calculate the total price
def calculate_total_price(quantity):
    if quantity > 10000:
        price_per_widget = 10
    elif quantity >= 5000:
        price_per_widget = 20
    else:
        price_per_widget = 30

    extended_price = quantity * price_per_widget
    tax_rate = 0.07
    tax_amount = extended_price * tax_rate
    total_price = extended_price + tax_amount

    return extended_price, tax_amount, total_price

# Input quantity of widgets
quantity = int(input("Enter the quantity of widgets: "))

# Calculate and display the results
extended_price, tax_amount, total_price = calculate_total_price(quantity)
print(f"Extended Price: ${extended_price}")
print(f"Tax Amount: ${tax_amount}")
print(f"Total Price: ${total_price}")