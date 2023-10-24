"""
CTI 110
P4LAB1A - 
boydj
10/12/23

"""

import turtle
import random

t = turtle.Turtle()
t.pensize(3)
# Set our variables - color, sides, size, and fill in or not
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

REPEAT = 10
for time in range(REPEAT):
  X = random.randrange(-200, 200)
  Y = random.randrange(-200, 200)
  t.penup()
  t.goto(X, Y)
  t.pendown()
  PEN_COLOR = random.choice(COLORS)
  SIDES = 3
  LENGTH = 100
  FILL = True
  FILL_COLOR = random.choice(COLORS)
  
  # Optional: let user pick
 # SIDES = int(input("How many sides?"))
  #LENGTH = int(input("How long is each side?"))
  SIDES = random.randrange(3, 12)
  LENGTH = random.randrange(10, 50)
  ANGLE = 360 / SIDES
  
  if FILL == True:
    t.begin_fill()
    t.fillcolor(FILL_COLOR)
  t.pencolor(PEN_COLOR)
  for side in range(SIDES):  
    # draw the side of the shape
    t.forward(LENGTH)
    t.right(ANGLE)
    # draw a star (kind of)
    for star_side in range(3):
      t.right(120)
      t.forward(LENGTH)
  if FILL == True:
    t.end_fill()
  
  # keep window open (at end)
  win = turtle.Screen()
  win.exitonclick()