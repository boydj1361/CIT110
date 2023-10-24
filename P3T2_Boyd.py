"""
CTI 110
P3T2 - Choices and Menus
boydj
9/26/23

"""
# The most simple program, with main()



def main():
   #my_function()
  print("-"*10, "Main Menu", "-"*10)
  print("1. Option one")
  print("2. Option two")
  print("3. Option three")

  # Let the user choose
  print("Your choice? ", end="")
  choice = int(input())
  print("You chose:", choice)

  # branch (if) on choice
  if choice ==1: 
   option_1()
  elif choice == 2:
    option_2()
  elif choice ==3:
    option_3()
  else:
    print("Sorry, that's not an option.")
 

def option_1():
  print("Ordering Lunch")
  print("Would you like a burger or a salad?")
  food = input()
  if food == "burger":
    print("One burger, coming up")
  elif food == "salad":
    print("Dressing on the side")
  else:
    print("We don't have any", food)
    

def option_2():
  print("What do you want on your hotdog?")
  top = input()
  if top == "ketchup":
    print("Hotdog with ketchup coming up.")
  elif top == "mustard":
    print("Hotdog with mustard coming up.")
  else:
    print("We don't have that sauce")

  
  

def option_3():
  print("Crocs or slides?")
  shoes = input()
  if shoes == "Crocs":
    print("Good Choice")
  elif shoes == "Slides":
    print("Good Choice")
  else:
    print("That's not an option.")
  
# start the program
main()