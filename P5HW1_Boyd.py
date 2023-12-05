# CTI 110
# P5HW1 - Quiz Show
# boydj
# 11/7/23

import random

def main_menu():
    print("Main Menu")
    print("-"*20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def addition_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 + num2
    user_answer = 0 # so it will always enter the while loop
    while user_answer != answer:
      user_answer = int(input(f"What is the sum of {num1} + {num2}? "))
      if user_answer == answer:
          print("Congratulations!!!! Your answer is correct! ")
      elif user_answer > answer:
          print("Sorry, guess is too high.")
          print("Try again: ")
      elif user_answer < answer:
          print("Sorry, guess is too low.")
          print("Try again: ")


def subtraction_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 - num2
    user_answer = 0
    while user_answer != answer:
      user_answer = int(input(f"What is the difference of {num1} - {num2}? "))
      if user_answer == answer:
        print("Congratulations!!!! Your answer is correct! ")
      elif user_answer > answer:
        print("Sorry, guess is too high.")
        print("Try again: ")
      elif user_answer < answer:
        print("Sorry, guess is too low.")
        print("Try again: ")


while True:
    main_menu()
    choice = int(input("Please choose one of the menu options: "))

    if choice == 1:
        addition_quiz()
    elif choice == 2:
        subtraction_quiz()
    elif choice == 3:
        print("Thank you for playing!! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")