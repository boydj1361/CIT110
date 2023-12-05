# CTI-110
# P4HW1 - Score List
# boydj
# 10/26/23

# CTI-110
# P4HW1 - Score List
# boydj
# 10/26/23

# CTI-110
# P4HW1 - Score List
# boydj
# 10/26/23

totalScores = 4
scores = []

print("How many scores do you want to enter: ", end="")
numScores = int(input())

for score in range(totalScores):
  print("Enter score #", score+1, ": ", end="")
  thisscore = float(input())
  while thisscore < 0 or thisscore > 100:
    print("Invalid. Score must be between 0 and 100.")
    print("Enter score #", score+1, ": ", end="")
    thisscore = float(input())
  scores.append(thisscore)

thisscore = sum(scores)
Average_score = thisscore / len(scores)
num_grade = Average_score

letter_grade = "G"
 
if num_grade > 90:
   letter_grade = "A"
elif num_grade >= 80:
  letter_grade = "B"
elif num_grade >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else:
  letter_grade = "F"

thisscore = sum(scores)
Lowest_score = min(scores)
Mod_List = scores.copy()
Average_score = thisscore / len(scores)

print("-"*5,"Results:","-"*5)
print("Lowest Score :", Lowest_score)
print("Modified List :", Mod_List)
print("Scores Average :", Average_score)
print("Grade :", Average_score, letter_grade)
print("-"*20)