# Driving Test Problem


# Subroutine to output pass or fail for driving test
def PassFail(MinorFaults):
  if MinorFaults < 16:
    return "pass"
  else:
    return "fail"


# Main program
print(PassFail(16))
