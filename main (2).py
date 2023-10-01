# Function to calculate price per ticket based on quantity
def calculate_price_per_ticket(quantity):
    if quantity >= 25:
        price_per_ticket = 50
    elif 10 <= quantity <= 24:
        price_per_ticket = 60
    elif 5 <= quantity <= 9:
        price_per_ticket = 70
    else:
        price_per_ticket = 75

    return price_per_ticket

# Input number of concert tickets
quantity = int(input("Enter the number of concert tickets: "))

# Calculate price per ticket
price_per_ticket = calculate_price_per_ticket(quantity)

# Calculate total cost
total_cost = quantity * price_per_ticket

# Display results
print(f"Number of Tickets: {quantity}")
print(f"Price Per Ticket: ${price_per_ticket}")
print(f"Total Cost: ${total_cost}")