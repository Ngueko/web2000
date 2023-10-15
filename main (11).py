# Initialize variables for sum, count, and cost per credit
total_tuition_owed = 0
student_count = 0
in_district_cost_per_credit = 250.00
out_of_district_cost_per_credit = 500.00

# Open the data file for reading
with open("student_data.txt", "r") as file:
    lines = file.read().splitlines()

# Iterate through the lines in the file
for i in range(0, len(lines), 3):
    last_name = lines[i]
    district_code = lines[i + 1]
    credits_taken = int(lines[i + 2])

    if district_code == 'I':
        tuition_owed = credits_taken * in_district_cost_per_credit
    else:
        tuition_owed = credits_taken * out_of_district_cost_per_credit

    total_tuition_owed += tuition_owed
    student_count += 1

    print("Last Name:", last_name)
    print("Credits Taken:", credits_taken)
    print("Tuition Owed:", tuition_owed)
    print()

# Display the sum of all tuition owed and the number of students
print("Sum of all Tuition Owed:", total_tuition_owed)
print("Number of Students:", student_count)