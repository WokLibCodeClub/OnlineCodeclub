from turtle import *
from random import randint

# ============= Screen ==============

screen = Screen()
screen.setup(400,400)
screen.bgpic('space-background.jpeg')

# Images
screen.register_shape('asteroid.png')
screen.register_shape('rocket.png')

# Animation control
screen.tracer(0)
screen.listen()

# ============= Rocket ==============


# ========== Rocks ==============


# ========== Scores & Lives =============

  
# ======= Win or lose ===================


# ============ Main loop ================

playing = True

while playing:
      
  # Update the picture
  screen.update()

