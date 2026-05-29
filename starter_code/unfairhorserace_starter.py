from turtle import *
from random import randint
from time import sleep

# ============= Set up Screen =============

WIDTH = 400
HEIGHT = 500

s = Screen()
s.setup(WIDTH, HEIGHT)
s.bgpic("background_pil.png")

s.register_shape("button", ((-26, -60),(26, -60),(26, 60),(-26, 60)))

# ======== Register dice images ==========

red_faces = ['blank', 'red1.png', 'red2.png', 'red3.png',
    'red4.png', 'red5.png', 'red6.png']
blue_faces = ['blank', 'blue1.png', 'blue2.png', 'blue3.png',
    'blue4.png', 'blue5.png', 'blue6.png']

# Register dice images and set up images in lists
for n in range(1,7):
  s.register_shape(red_faces[n])
  s.register_shape(blue_faces[n])

# ======== Create horse turtles =========

horses = []

horse_colours = ["red", "cyan", "green", "blue", "orange"]

for n in range(13):
  horses.append(Turtle())
  horses[n].speed(9)
  horses[n].hideturtle()
  horses[n].penup()
  horses[n].shape("circle")
  horses[n].speed(3)

# ======= Create button turtle =========

button = Turtle()
button.hideturtle()
button.penup()
button.shape("button")
button.color("gray")
button.goto(-100, -218)
button.stamp()
button.fillcolor('')
button.showturtle()

button_text = Turtle()
button_text.hideturtle()
button_text.penup()
button_text.goto(-100, -226)
button_text.color("white")
button_text.write("click to roll dice", font = ("arial", 11, "bold"), align = "center")

# ======== Create dice turtles =========

red_die = Turtle()
red_die.hideturtle()
red_die.speed(0)
red_die.shape(red_faces[randint(1,6)])
red_die.penup()
red_die.goto(40, -220)
red_die.showturtle()


# ============ Functions ============

def roll_dice():
  for _ in range(6):
    r = randint(1,6)
    red_die.shape(red_faces[r])
    sleep(0.15)
  return r
    
def move_horse(x,y):
  n = roll_dice()
  sleep(0.5)

# ==== Set up before Main loop =====

winner = False

button.onclick(move_horse)

# =========== Main loop ============

while not winner:
  pass

# ======== after Main loop =========

button.onclick(None)

