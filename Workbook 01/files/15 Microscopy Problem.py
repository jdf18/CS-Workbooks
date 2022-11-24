# Microscopy Problem

actual_size = 80
image_size = 4

def find_magnification(actual, image):
  magnification = actual*10000/image
  return magnification

magnification = find_magnification(actual_size, image_size)

print("The magnification is "+str(magnification)+"X")