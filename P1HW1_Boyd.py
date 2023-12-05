"""
CTI110
P1HW1 - Variables
boydj
9/5/23

Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them

"""
# PART ONE: VARIABLES
# variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input, then convert it to int
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("Enter another interget:")
second = int(input())
# TODO: print the number, not the words first and second
print(first, "+", second, "=", first + second)
print(first, "*", second, "=", first * second)

# PART TWO: MOVIES
# Three variables
# string - movie name
# int - the year of the movie
# float - the gross (in million dollars)
# string - a quote
name = "Fast X"
year = 2023
gross = 704,709,660

# Print out this information
# The print a movie quote

print("Movie name:", name)
print("Movie came out in:", year)
print("The Gross:", gross)
print("A Quote: Dominic Toretto: You might have won, Dante, but I have something you don't. Dante: Yeah? What's that? [Dom stares down a keg of Corona] Dominic Toretto: Family.")




