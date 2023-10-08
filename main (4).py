def main():
    continue_program = input("Do you want to continue (Yes/No)? ").strip().lower()
    discount_total = 0
    
    while continue_program == "yes":
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        
        extended_price = quantity * price
        
        if extended_price > 10000.00:
            discount_percent = 0.25
        else:
            discount_percent = 0.10
        
        discount_amount = extended_price * discount_percent
        total = extended_price - discount_amount
        
        print("Extended Price:", extended_price)
        print("Discount Amount:", discount_amount)
        print("Total:", total)
        
        discount_total += discount_amount
        
        continue_program = input("Do you want to enter another order (Yes/No)? ").strip().lower()
    
    print("Sum of all discounts:", discount_total)

if __name__ == "__main__":
    main()