class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  def calculate_bonus(self, bonus_rate):
      return self.salary * bonus_rate

# Creating an instance of Employee
employee = Employee("John Doe", 50000)

# Testing the bonus calculation
bonus_rate = 0.10  # 10% bonus rate
bonus = employee.calculate_bonus(bonus_rate)
print(f"Bonus for {employee.name}: ${bonus}")