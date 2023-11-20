# Array of last names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Function to display names
def display_names(names):
    for name in names:
        print(name)

# Function to display names in reverse order
def display_names_reverse(names):
    for name in reversed(names):
        print(name)

# Test the functions
print("Original Order:")
display_names(last_names)

print("\nReverse Order:")
display_names_reverse(last_names)