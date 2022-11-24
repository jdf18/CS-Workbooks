# Ball Pit Problem
from math import pi

PACKING_DENSITY = 0.75

def radius(diameter):
  return diameter / 2


def area(radius):
  return pi * (radius)**2

def circumerence(diameter):
  return pi * diameter

def volume(radius):
  return 4/3 * pi * (radius**3)

def calculate_balls(pit_radius, height, ball_size):
  pit_volume = area(pit_radius) * height
  ball_volume = volume(radius(ball_size))
  return pit_volume / ball_volume * PACKING_DENSITY

print(calculate_balls(1,0.2,0.05))
