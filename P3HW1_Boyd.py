# CTI 110
# P3HW1 - Letter Grades
# boydj
# 10/8/23

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))

grades = (mod_1, mod_2, mod_3, mod_4, mod_5)
num = 5
sum = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5)
average = sum / num

if average > 90:
  letter_grade = "A"
elif average >= 80:
  letter_grade = "B"
elif average >= 70:
  letter_grade = "C"
elif average >= 60:
  letter_grade = "D"
else:
  letter_grade = "F"

print("A grade of", average, "is a", letter_grade)