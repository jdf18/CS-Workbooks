# Nitrate Problem

# When keeping fish, one of the goals to reduce algae is to 
#  keep nitrates to a minimum. One way of doing this is to dose 
#  a carbon source which nitrifying bacteria within an aquarium 
#  consume together with nitrates. The carbon source must be dosed very precisely.
# Write this function to determine and return the dose.
# The program should output:
#  “For x nitrate dose y ml”
# Where x is the parameter and y is the returned value.

def calculate_dosage(nitrate: float) -> int:
    if nitrate > 10:
        return 3
    elif nitrate > 2.5:
        return 2
    elif nitrate > 1:
        return 1
    return 0.5

def program():
    n = input("Enter amount of nitrate: ")
    dosage = calculate_dosage(n)
    print(f"For {n} nitrate dose {dosage} ml")