def calculate_discount_and_discounted_price(quantity, price, discount_rate):
  original_total = quantity * price
  discount_amount = (discount_rate / 100) * original_total
  discounted_price = original_total - discount_amount
  return discount_amount, discounted_price

def main():
  # User input
  quantity = float(input("Enter the quantity of the item: "))
  price = float(input("Enter the price of the item: "))
  discount_rate = float(input("Enter the discount rate (as a percentage): "))

  # Calculate discount and discounted price
  discount_amount, discounted_price = calculate_discount_and_discounted_price(quantity, price, discount_rate)

  # Display results
  print(f"Quantity: {quantity}")
  print(f"Price: {price}")
  print(f"Discount Amount: {discount_amount}")
  print(f"Discounted Price: {discounted_price}")

if __name__ == "__main__":
  main()