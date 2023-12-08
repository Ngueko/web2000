class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      if self.district_code == 'I':
          rate = 250.00
      else:
          rate = 500.00
      return self.enrolled_credits * rate

# Testing the Student class
student1 = Student("Jane", "Doe", "I", 12)  # In-district student
student2 = Student("John", "Smith", "O", 10)  # Out-of-district student

# Calculating tuition
tuition1 = student1.compute_tuition()
tuition2 = student2.compute_tuition()

print(f"Tuition for {student1.first_name} {student1.last_name}: ${tuition1}")
print(f"Tuition for {student2.first_name} {student2.last_name}: ${tuition2}")