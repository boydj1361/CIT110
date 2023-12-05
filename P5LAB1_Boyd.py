# CTI 110
# P5LAB1 - CYOA
# boydj
# 10/26/23
# Feel free to fork this REPL and make changes.

# first function: main_menu().

def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        choice_back_door()
        # Call choice 2 here (You can add the corresponding function)
        pass
    elif choice == '3':
        choice_go_home()
        # Call choice 3 here (You can add the corresponding function)
        pass
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("the door is cracked with a warning sign on it...")
    print("Do you:")
    print("1. Go inside")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
      choice_inside_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_back_door()
  
def choice_inside_door():
    print("You're inside the house.")
    print("There's a note on the table.")
    print("Do you:")
    print("1. Pick up and read the note?")
    print("2. Leave it and go home")
    choice = input("Choose: ")
    if choice == '1':
      choice_read_note()
    elif choice == '2':
      choice_go_home()
    else:
      print("You have to choose...")
      choice_inside_door()

def choice_read_note():
    print("You pick up the note and read it.")
    print("It says:")
    print("Look behind you...")
    print("There seems to also be a key to the front door..")
    print("Do you:")
    print("1. Pick up the key and leave")
    print("2. Listen to the note and look behind you")
    choice = input("Choose: ")
    if choice == '1':
      choice_key()
    elif choice == '2':
      choice_look_behind()
    else:
      print("You have to choose...")
      choice_read_note()

def choice_key():
    print("You chose to be safe and take the key to leave.")
  
def choice_look_behind():
    print("You looked behind you and...")
    print("You died..")
    
    
    

def choice_go_home():
    print("You chose to go home.")

# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")

#start the program
main()
