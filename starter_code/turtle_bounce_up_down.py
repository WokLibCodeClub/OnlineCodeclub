from turtle import *
from time import sleep
from random import randint

s = Screen()
s.setup(400,360)
s.register_shape("walls_ew.png")
s.bgpic("walls_ew.png")

t = Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)

# CHANGE DIRECTION BETWEEN up AND down
direction = "up"

# set turtle heading
if direction == "up":
  t.setheading(randint(30,150))
elif direction == "down":
  t.setheading(randint(210,330))

if direction == "up":
  while t.ycor() < 78:
    t.forward(2)
elif direction == "down":
  while t.ycor() > -78:
    t.forward(2)

# set turtle heading to minus previous heading
t.setheading(-t.heading())

while t.ycor() != 0:
  t.forward(2)

# COPY FOUR LINES TO FUNCTION move_person(t) (REMOVING THE FIRST HASHES)
#  # if person gets close to top or bottom edge
#  if t.ycor() > HEIGHT/2 or t.ycor() < -HEIGHT/2+30:
#    # reverse heading
#    t.setheading(-t.heading())
