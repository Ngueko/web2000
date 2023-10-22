# Define a function to calculate batting average.
def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0  # Avoid division by zero
    batting_average = hits / at_bats
    return batting_average

# Initialize variables.
player_count = 0

# Create an empty dictionary to store player data.
players = {}

# Continue taking user input until Ctrl+Z (EOFError) is pressed.
try:
    while True:
        # Ask the user for player information.
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))

        # Calculate the batting average.
        batting_average = calculate_batting_average(hits, at_bats)

        # Store the player's last name and batting average in the dictionary.
        players[last_name] = batting_average

        # Increment the player count.
        player_count += 1

        # Display last name and batting average.
        print(f"Player: {last_name}, Batting Average: {batting_average:.3f}")

except EOFError:
    pass  # Ctrl+Z pressed, exit the loop

# Display the total number of players entered.
print(f"Total number of players entered: {player_count}")

# Display the players and their batting averages.
print("Player Data:")
for last_name, batting_average in players.items():
    print(f"Player: {last_name}, Batting Average: {batting_average:.3f}")