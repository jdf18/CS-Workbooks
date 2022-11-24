# Energy bill calculator

RATE = 2.84


def energy_cost(previous_reading, current_reading, cal_value):
  units_used = current_reading - previous_reading
  kWh = units_used * 1.022 * (cal_value / 3.6)
  return RATE * kWh


calorific_value = 39.3
p_reading = float(input("Previous reading: "))
c_reading = float(input("Current reading: "))
cost = energy_cost(p_reading, c_reading, calorific_value)
print("This will cost £%s" % cost)
