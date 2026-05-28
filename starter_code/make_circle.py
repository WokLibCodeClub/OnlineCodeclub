from math import sin, cos, radians

def circle_coords(radius):
  # create empty list for coordinates
  small_circle_coords = []
  
  # loop through circle in 30 degree increments
  for theta in range(0,361,30):
    #print(theta)
    x = round(radius * cos(radians(theta)))
    y = round(radius * sin(radians(theta)))
    # append coordinates to list
    small_circle_coords.append((y,x))
    
  #print(small_circle_coords)
  return tuple(small_circle_coords)
