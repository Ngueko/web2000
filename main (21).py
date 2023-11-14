# Global variables
total = 0
tax = 0

def calculate_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = 0.07 * total

def main():
    # User input
    quantity = float(input("Enter the quantity of the item: "))
    unit_price = float(input("Enter the unit price of the item: "))

    # Calculate total and tax
    calculate_total_and_tax(quantity, unit_price)

    # Display results
    print(f"Total: {total}")
    print(f"Tax: {tax}")

if __name__ == "__main__":
    main()