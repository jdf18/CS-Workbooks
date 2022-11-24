# Fish Tank Problem

width = 15
height = 10
length = 20

def find_volume(l,h,w):
  return l * h * w / 1000

V = find_volume(length, height, width)
print("The volume of the tank is "+str(V)+" litres")