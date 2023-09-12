import matplotlib.pyplot as plt

# Collect the data
data = [] # empty list
"""

print("Enter Pokeman data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())
"""
# New Version - loop and get each dat at a time\
num_days = int(input("How many days?"))
for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) # add it to the end of the list
  
# put the data in a list (Done)
# print min and max
print("Best day:", max(data))
print("Worst day:", min(data))
# don't do total and average yet    
# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()

