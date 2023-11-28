# Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# Display the list of players before sorting
print("List of players before sorting:", players)

# Sort the list of players
players.sort()

# Display the sorted list of players
print("List of players after sorting:", players)

# Make a copy of the list of players
players2 = players.copy()  # Alternatively, use players2 = players[:]

# Display the copied list of players
print("Copied list of players (players2):", players2)

# Reverse the order of players2
players2.reverse()

# Display the original list of players
print("Original list of players (players):", players)

# Display players2 after reversing
print("List of players2 after reversing:", players2)