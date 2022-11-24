# Using variables and constants

# Subroutine to calculate price
def FlowRate(Volume, Time):
    return Volume / Time * 60

# Main program
Volume = 100
Time = 30
Heart = FlowRate(Volume, Time)
print("The flow rate of the human heart is", Heart, "ml/s")
