def load_data(filename):
  names = []
  scores = []
  with open(filename, 'r') as file:
      for line in file:
          name, score = line.strip().split(',')  # Adjust the delimiter if necessary
          names.append(name)
          scores.append(int(score))
  return names, scores

def find_highest_and_lowest(names, scores):
  high_var = 0
  low_var = 999
  high_index = low_index = 0

  for i, score in enumerate(scores):
      if score > high_var:
          high_var = score
          high_index = i
      if score < low_var:
          low_var = score
          low_index = i

  print(f"Highest Score: {names[high_index]} with a score of {high_var}")
  print(f"Lowest Score: {names[low_index]} with a score of {low_var}")

# Assuming the data file is named 'students_scores.txt'
last_names, exam_scores = load_data('students_scores.txt')
find_highest_and_lowest(last_names, exam_scores)