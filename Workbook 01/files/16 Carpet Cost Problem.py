# Carpet cost program

UNDERLAY_UNIT_COST = 3
GRIPPERS_UNIT_COST = 1

FITTING_FEE = 50


def carpet_cost(width, length, unit_cost):
  return width * length * unit_cost


def underlay_cost(width, length):
  return width * length * UNDERLAY_UNIT_COST


def grippers_cost(width, length):
  return (width * 2 + length * 2) * GRIPPERS_UNIT_COST


def total_price(width, length, unit_cost):
  total = FITTING_FEE
  total += carpet_cost(width, length, unit_cost)
  total += underlay_cost(width, length)
  total += grippers_cost(width, length)
  return total


width = 7
length = 6
unit_cost = 17
total = total_price(width, length, unit_cost)
print("The total price is £%s" % total)
