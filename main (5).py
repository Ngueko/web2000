def main():
    continue_program = input("Do you want to continue (Yes/No)? ").strip().lower()
    gross_pay_total = 0
    employee_count = 0

    while continue_program == "yes":
        last_name = input("Enter employee last name: ")
        hours_worked = float(input("Enter hours worked: "))
        rate_of_pay = float(input("Enter rate of pay: "))

        if hours_worked > 40:
            gross_pay = 40 * rate_of_pay + (hours_worked - 40) * rate_of_pay * 1.5
        else:
            gross_pay = hours_worked * rate_of_pay

        print("Employee Last Name:", last_name)
        print("Gross Pay:", gross_pay)

        gross_pay_total += gross_pay
        employee_count += 1

        continue_program = input("Do you want to enter another employee (Yes/No)? ").strip().lower()

    print("Total Gross Pay:", gross_pay_total)
    print("Total Number of Employees:", employee_count)
    
    if employee_count > 0:
        print("Average Pay:", gross_pay_total / employee_count)
    else:
        print("No employees entered, so the average pay cannot be calculated.")

if __name__ == "__main__":
    main()