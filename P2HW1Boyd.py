"""
CTI 100
P2HW1 - Travel
boydj
9/14/23

"""
initial_budget = float(input("What's your initial budget? "))
location = input("Travel Destination: ")
gas = float(input("How much would you think you will spend on gas? "))
hotel = float(input("How much will you need for a hotel? "))
food = float(input("How much will you need for food? "))

print ("Travel Destination:", location)
print ("Initial budget:$", initial_budget)
print ("Gas:$", gas)
print ("hotel:$", hotel)
print ("food:$", food)

remaining_balance = initial_budget - gas - hotel - food
print ("Remaining Balance:$", remaining_balance)

