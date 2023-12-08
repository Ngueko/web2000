class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  def calculate_bonus(self, bonus_rate):
      return self.salary * bonus_rate

class Manager(Employee):
  def __init__(self, name, salary):
      super().__init__(name, salary)

  def calculate_long_term_bonus(self):
      return self.salary * 0.40

# Testing the Manager class
manager = Manager("Alice Johnson", 80000)

# Demonstrating inherited and new methods
regular_bonus = manager.calculate_bonus(0.10)  # 10% regular bonus
long_term_bonus = manager.calculate_long_term_bonus()

print(f"Regular Bonus for {manager.name}: ${regular_bonus}")
print(f"Long Term Bonus for {manager.name}: ${long_term_bonus}")