# Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# Display the list of grades
print("List of grades:", grades)

# Count and display the number of 'A' grades
count_a = grades.count("A")
print("Number of 'A' grades:", count_a)

# Find and display the index of the first 'B' grade
if "B" in grades:
    index_b = grades.index("B")
    print("Index of the first 'B' grade:", index_b)
else:
    print("There is no 'B' grade in the list.")

# Check for the presence of 'F' grade in the list
if "F" not in grades:
    print("F is not in the list.")

# Assuming second_list is already defined and filled with values
second_list = [500, 600, 700, 800, 900]

# Clear the second list
second_list.clear()

# Display the cleared second list
print("Second list after being cleared:", second_list)

# Delete the second list
del second_list

# Try to display the second list (this will cause an error)
try:
    print("Second list:", second_list)
except NameError as e:
    print("Error:", e)