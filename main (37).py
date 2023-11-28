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
    print("There is no 'B' grade in the list."