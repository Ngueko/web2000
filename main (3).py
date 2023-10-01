# Function to calculate bonus rate based on job level
def calculate_bonus_rate(job_level):
    if job_level >= 10:
        bonus_rate = 0.25
    elif 5 <= job_level <= 9:
        bonus_rate = 0.20
    else:
        bonus_rate = 0.10

    return bonus_rate

# Input employee information
last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: $"))
job_level = int(input("Enter employee job level: "))

# Calculate bonus rate
bonus_rate = calculate_bonus_rate(job_level)

# Calculate bonus
bonus = salary * bonus_rate

# Display results
print(f"Employee Last Name: {last_name}")
print(f"Bonus: ${bonus}")