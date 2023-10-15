a, b = 1, 1

# Print the first two numbers (1, 1)
print(a)
print(b)

# Use a for loop to compute and print the next 18 numbers in the sequence
for _ in range(18):
    # Compute the next number in the sequence
    next_number = a + b

    # Print the next number
    print(next_number)

    # Update the values of a and b for the next iteration
    a, b = b, next_number