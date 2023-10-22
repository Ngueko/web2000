# Define a function to calculate miles per gallon (MPG).
def calculate_mpg(miles, gallons):
    if gallons == 0:
        return 0.0  # Avoid division by zero
    mpg = miles / gallons
    return mpg

# Initialize variables.
trip_count = 0

# Create empty lists to store trip data.
destinations = []
miles_traveled = []
gallons_used = []

# Continue taking user input until Ctrl+Z (EOFError) is pressed.
try:
    while True:
        # Ask the user for trip information.
        destination = input("Enter destination city: ")
        miles = float(input("Enter miles traveled: "))
        gallons = float(input("Enter gallons used: ")

        # Calculate the MPG.
        mpg = calculate_mpg(miles, gallons)

        # Store trip data in lists.
        destinations.append(destination)
        miles_traveled.append(miles)
        gallons_used.append(gallons)

        # Increment the trip count.
        trip_count += 1

        # Display trip information (destination, miles, and MPG).
        print(f"Trip {trip_count}: Destination: {destination}, Miles: {miles:.2f}, MPG: {mpg:.2f}")

except EOFError:
    pass  # Ctrl+Z pressed, exit the loop

# Display the total number of trips entered.
print(f"Total number of trips entered: {trip_count}")

# Display trip data.
print("Trip Data:")
for i in range(trip_count):
    print(f"Trip {i + 1}: Destination: {destinations[i]}, Miles: {miles_traveled[i]:.2f}, MPG: {calculate_mpg(miles_traveled[i], gallons_used[i]):.2f}")