from turtle import *
from random import randint

#############################################
# VARIABLES
#############################################

screen = Screen()
screen.setup(500,400)
screen.bgcolor(255,200,150)

# Create turtle to draw background
bg = Turtle()
bg.hideturtle()
bg.penup()
bg.speed(0)

# Create turtle to count number of matches remaining
tally = Turtle()
tally.hideturtle()
tally.penup()
tally.speed(0)
tally.color("red")

# Choose which player to go first at random
next_go = randint(0,1)

# List of players
players = ["Princess Leia", "The Fonz"]

instructions = ["On your turn take one, two or three matches. ",
               "The player who takes the last match loses."]
               

#############################################
# FUNCTIONS
#############################################

# Draw instructions, and Player names
def draw_bg():
  tracer(0)
  bg.color("red")
  y_text = 170
  for i in range(len(instructions)):
    bg.goto(-220, y_text)
    bg.write(instructions[i], font = ("Arial", 11, "normal"))
    y_text -= 24

  bg.color("black")
  x_text = -75
  for n in players:
    bg.goto(x_text, -60)
    bg.write(n, font = ("Arial", 13, "bold"), align = "center")
    x_text += 150
  tracer(1)    

#############################################
# MAIN CODE
#############################################

draw_bg()

print("******************************\n" )

