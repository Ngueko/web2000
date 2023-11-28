# Initialize an empty list
numbers_list = []

# Uncomment this section to prompt the user for the number of items
# num_items = int(input("Enter the number of items: "))

# Replace 'num_items' in the loop with the variable above after uncommenting
for i in range(3):  # Use 'num_items' here instead of 3 after testing
    # Uncomment the line below to get user input
    # num = int(input(f"Enter number {i+1}: "))
    num = i + 1  # Temporary line for testing, remove after uncommenting above line
    numbers_list.append(num)

# Display the list before insertion
print("The list of numbers before insertion:", numbers_list)

# Insert the score of 99 at position 1
numbers_list.insert(1, 99)

# Display the list after insertion
print("The list of numbers after inserting 99 at position 1:", numbers_list)

# Check if 99 is in the list and replace it with 100
if 99 in numbers_list