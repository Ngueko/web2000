def calculate_commission_and_target(sales):
  if sales > 100000:
      commission_rate = 0.10
  else:
      commission_rate = 0.05

  commission = commission_rate * sales
  next_year_target = 0.05 * sales
  return commission, next_year_target

def main():
  # User input
  last_name = input("Enter the salesperson's last name: ")
  sales = float(input("Enter the sales amount: "))

  # Calculate commission and next year's target
  commission, next_year_target = calculate_commission_and_target(sales)

  # Display results
  print(f"Salesperson Name: {last_name}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${next_year_target:.2f}")

if __name__ == "__main__":
  main()