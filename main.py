$ git mv main.py P2LAB1_LombardiDillan.py

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):

  gallon_used = driven_miles / miles_per_gallon

  cost = gallon_used * dollars_per_gallon  

  return cost  

miles_per_gallon = float(input(""))

dollars_per_gallon = float(input(""))

cost1 = driving_cost(20, miles_per_gallon, dollars_per_gallon)

cost2 = driving_cost(75, miles_per_gallon, dollars_per_gallon)

cost3 = driving_cost(500, miles_per_gallon, dollars_per_gallon)

print("%.2f" % cost1, "%.2f" % cost2, "%.2f" % cost3)

