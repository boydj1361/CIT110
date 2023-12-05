# CTI 110
# P2HW2 - List
# boydj
# 9/21/23
data = []

M1 = int(input('Enter grade for Module 1: '))
M2 = int(input('Enter grade for Module 2: '))
M3 = int(input('Enter grade for Module 3: '))
M4 = int(input('Enter grade for Module 4: '))
M5 = int(input('Enter grade for Module 5: '))
M6 = int(input('Enter grade for Module 6: '))

grades = [M1, M2, M3, M4, M5, M6]
total = M1 + M2 + M3 + M4 + M5 + M6
a = 6
average = total / a

print( "-"*5,"Results:","-"*5)
print("Lowest Grade:", min(grades))
print("Highest Grade:", max(grades))
print('Sum of Grades:', total)
print("Average:", average)
print("-"*20)