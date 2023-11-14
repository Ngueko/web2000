def calculate_averages(score1, score2, score3, handicap):
  average_score = (score1 + score2 + score3) / 3
  average_score_with_handicap = average_score + handicap
  return average_score, average_score_with_handicap

def main():
  # User input
  last_name = input("Enter the bowler's last name: ")
  score1 = int(input("Enter score for game 1: "))
  score2 = int(input("Enter score for game 2: "))
  score3 = int(input("Enter score for game 3: "))
  handicap = int(input("Enter the handicap: "))

  # Calculate averages
  average_score, average_score_with_handicap = calculate_averages(score1, score2, score3, handicap)

  # Display results
  print(f"Bowler's Last Name: {last_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Average Score with Handicap: {average_score_with_handicap:.2f}")

if __name__ == "__main__":
  main()