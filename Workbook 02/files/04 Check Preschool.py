# Check pre-school elegibility program

# Selection commands


# Subroutine to validate age
def ValidAge(age):
  if 2 <= age <= 5:
    print("Elegibile for pre-school")
  else:
    print("Not elegibile for pre-school")


# Main program
ValidAge(-5)
ValidAge(0)
ValidAge(1)
ValidAge(2)
ValidAge(3)
ValidAge(5)
ValidAge(7)
