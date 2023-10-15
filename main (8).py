# Initialize variables for accumulated interest and the year counter
accumulated_interest = 0
year = 1

# Get the principal amount and interest rate from the user
principal = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate (as a decimal): "))

# Print the table header
print("Year\tBeginning Balance\tEnding Balance")

# Run the loop for 5 years
while year <= 5:
    # Calculate annual interest and ending balance
    annual_interest = principal * interest_rate
    ending_balance = principal + annual_interest

    # Display the year, beginning balance, and ending balance
    print(f"{year}\t${principal:.2f}\t\t${ending_balance:.2f}")

    # Accumulate the interest
    accumulated_interest += annual_interest

    # Set the new principal for the next year
    principal = ending_balance

    # Increment the year
    year += 1

# Display the total accumulated interest
print(f"Total interest earned: ${accumulated_interest:.2f}")