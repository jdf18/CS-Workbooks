# Key Stage Program

# Selection commands


# Subroutine to output Key Stage
def YearGroup(Year):
  if Year >= 1 and Year < 3:
    print("Key Stage 1")
  elif Year >= 3 and Year < 7:
    print("Key Stage 2")
  elif Year >= 7 and Year < 10:
    print("Key Stage 3")
  elif Year >= 10 and Year < 12:
    print("Key Stage 4")
  elif Year >= 12 and Year < 15:
    print("Sixth Form")


# Main program
YearGroup(7)
YearGroup(11)
YearGroup(6)
YearGroup(13)
