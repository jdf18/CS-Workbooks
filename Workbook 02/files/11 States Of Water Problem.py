# States of water problem


def state_constructor(melting_point: float, boiling_point: float):

  def foo(temp: float):
    if temp <= melting_point:
      print("Solid")
      return
    elif temp >= boiling_point:
      print("Gaseous")
      return
    print("Liquid")

  return foo


state_of_water = state_constructor(0, 100)
state_of_water(37.2)
