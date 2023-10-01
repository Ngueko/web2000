# Function to calculate interest rate based on principle and years
def calculate_interest_rate(principle, years_to_maturity):
    if principle > 100000:
        interest_rate = 0.06
    elif 50000 <= principle <= 100000:
        if years_to_maturity == 10:
            interest_rate = 0.05
        elif years_to_maturity == 5:
            interest_rate = 0.04
    else:
        interest_rate = 0.02

    return interest_rate

# Input principle and years to maturity
principle = float(input("Enter the principle amount: $"))
years_to_maturity = int(input("Enter the years to maturity: "))

# Calculate interest rate
interest_rate = calculate_interest_rate(principle, years_to_maturity)

# Calculate first-year interest
first_year_interest = principle * interest_rate

# Display results
print(f"Principle: ${principle}")
print(f"Interest Rate: {interest_rate * 100}%")
print(f"Interest Amount for First Year: ${first_year_interest}")