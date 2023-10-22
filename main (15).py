# Define a function to calculate tuition owed.
def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        tuition = credit_hours * 250
    elif district_code == "O":
        tuition = credit_hours * 550
    else:
        tuition = 0  # Invalid district code, set tuition to 0
    return tuition

# Initialize variables.
total_tuition = 0.0

# Create an empty list to store student data.
students = []

# Continue taking user input until Ctrl+Z (EOFError) is pressed.
try:
    while True:
        # Ask the user for student information.
        last_name = input("Enter student's last name: ")
        credit_hours = int(input("Enter credit hours: "))
        district_code = input("Enter district code (I for in-district, O for out-of-district): ")

        # Calculate the tuition owed.
        tuition = calculate_tuition(credit_hours, district_code)

        # Store student data in a list.
        student_data = {
            "last_name": last_name,
            "tuition": tuition
        }
        students.append(student_data)

        # Add tuition to the total.
        total_tuition += tuition

        # Display student name and tuition owed.
        print(f"Student: {last_name}, Tuition Owed: ${tuition:.2f}")

except EOFError:
    pass  # Ctrl+Z pressed, exit the loop

# Display the total tuition owed for all students.
print(f"Total Tuition Owed: ${total_tuition:.2f}")

# Display student data.
print("Student Data:")
for student_data in students:
    print(f"Student: {student_data['last_name']}, Tuition Owed: ${student_data['tuition']:.2f}")