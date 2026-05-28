from turtle import *
from time import sleep
from random import randint

s = Screen()
s.setup(400,360)
s.register_shape("walls_ns.png")
s.bgpic("walls_ns.png")

t = Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)

# CHANGE DIRECTION BETWEEN left AND right
direction = "right"

# set turtle heading
if direction == "left":
  t.setheading(randint(120,240))
elif direction == "right":
  t.setheading(randint(-60,60))

if direction == "right":
  while t.xcor() < 78:
    t.forward(2)
elif direction == "left":
  while t.xcor() > -78:
    t.forward(2)

# set turtle heading to ?????????????????????
#t.setheading(????????????)

while t.xcor() != 0:
  t.forward(2)
