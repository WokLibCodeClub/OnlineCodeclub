from turtle import *
from random import randint
from time import sleep
from make_circle import circle_coords

# ============= Set up Screen =============

WIDTH = 400
HEIGHT = 360

s = Screen()
s.setup(WIDTH, HEIGHT)
s.bgcolor("lightcyan")

tracer(0)

small_circle_radius = 6

small_circle_coordinates = circle_coords(small_circle_radius)

s.register_shape("small_circle", small_circle_coordinates)

# ============= Person turtle =============

def create_person():
  a = Turtle()
  a.hideturtle()
  a.shape("small_circle")
  a.color("blue")
  a.penup()
  a.setheading(randint(0,360))
  a.goto(randint(-WIDTH/2, WIDTH/2),randint(-HEIGHT/2+30, HEIGHT/2))
  a.showturtle()
  return a

def move_person(t):
  # small random change to heading
  t.setheading(t.heading() + randint(-30, 30))
  t.forward(3)

# ============= Counter turtle ============

counter = Turtle()
counter.penup()
counter.hideturtle()
counter.goto(WIDTH/2-160, -HEIGHT/2+10)

def update_count():
  counter.clear()
  counter_string = "Time: " + str(clock_now)
  counter.write(counter_string, font = ("Arial", 8, "normal"), align = "left")

# ======== Setup before main loop =========

clock_now = 0

people = []

create_person()

# =============== Main loop ===============

while clock_now <= WIDTH:
  update_count()
  update()
  clock_now += 1
  sleep(0.05)
