# Case Study 6 : Manufacturing Cost and Profitability Analysis
material = float(input("Material Cost: "))
labor = float(input("Labor Cost: "))
overhead = float(input("Overhead Cost: "))
units = int(input("Units Produced: "))

total_cost = material + labor + overhead
profit = total_cost * 0.20

selling_price = (total_cost + profit) / units

print("Total Cost =", total_cost)
print("Profit =", profit)
print("Selling Price per Unit =", selling_price)