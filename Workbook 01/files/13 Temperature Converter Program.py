# Temperature converter problem

# Subroutine to convert Centigrade to Fahrenheit
def CtoF(C):
  return (C * 1.8) + 32

# Subroutine to convert Fahrenheit to Centigrade
def FtoC(F):
	return (F - 32) / 1.8

# Main program
C = 30
F = CtoF(C)
print(C,"degrees C is",F,"degrees F")
