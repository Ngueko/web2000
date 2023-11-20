Smith,0.267
Johnson,0.300
Williams,0.285
...def load_data(filename):
  player_names = []
  averages = []
  with open(filename, 'r') as file:
      for line in file:
          name, average = line.strip().split(',')
          player_names.append(name)
          averages.append(float(average))
  return player_names, averages

def display_data(names, averages):
  for name, average in zip(names, averages):
      print(f"{name}: {average}")

def search_player(names, averages, search_name):
  if search_name in names:
      index = names.index(search_name)
      print(f"{names[index]}: {averages[index]}")
  else:
      print("Player not found.")

# Load data from file
player_names, batting_averages = load_data('player_averages.txt')

# Display player names and averages
display_data(player_names, batting_averages)

# Repeatedly ask the user for a last name and search
while True:
  last_name = input("Enter a player's last name to search (or 'quit' to exit): ").strip()
  if last_name.lower() == 'quit':
      break
  search_player(player_names, batting_averages, last_name)