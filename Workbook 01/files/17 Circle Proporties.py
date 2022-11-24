# Circle Proporites Problem
from math import pi

diameter = float(input("Diameter: "))
arc_angle = float(input("Arc angle: "))


def radius(diameter):
  return diameter / 2


def area(diameter):
  return pi * (radius(diameter))**2


def circumerence(diameter):
  return pi * diameter


def arc_length(circumference, arc_angle):
  return circumference * arc_angle


print("Radius: %s" % radius(diameter))
print("Area: %s" % area(diameter))
print("Crcumference: %s" % circumerence(diameter))
print("Arc Length: %s" % arc_length(diameter, circumerence(diameter)))
