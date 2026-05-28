# ============== Import libraries =============
from turtle import *
from time import sleep
from random import randint

# =============== Set up screen ===============
s = Screen()
s.setup(400,360)
s.register_shape("angles.png")
s.bgpic("angles.png")

# =============== Make a turtle ===============
t = Turtle()
t.shape("turtle")
t.color("red")

# ============= Set turtle heading ============
t.setheading(40)
# pause three seconds
sleep(3)

# =========== Change turtle heading ===========
# add a number to turtle heading
t.setheading(t.heading() + 70)

