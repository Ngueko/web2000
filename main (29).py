def search_player(names, averages, search_name):
    if search_name in names:
        index = names.index(search_name)
        print(f"{names[index]}: {averages[index]}")
    else:
        print("Name not found.")  # Modified line

# The rest of the code remains the same