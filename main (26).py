# Array of last names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Array of exam scores (parallel to last_names)
exam_scores = [87, 92, 78, 85, 93, 88, 79, 84, 91, 86]

# Function to display names and scores
def display_names_and_scores(names, scores):
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

# Function to display names and scores in reverse order
def display_names_and_scores_reverse(names, scores):
    for name, score in zip(reversed(names), reversed(scores)):
        print(f"{name}: {score}")

# Test the functions
print("Original Order:")
display_names_and_scores(last_names, exam_scores)

print("\nReverse Order:")
display_names_and_scores_reverse(last_names, exam_scores)