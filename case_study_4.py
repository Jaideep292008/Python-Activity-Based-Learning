# Case Study 4 : Railway Fare Calculator
distance = float(input("Enter distance: "))
age = int(input("Enter age: "))
travel_class = int(input("1-Sleeper 2-AC3 3-AC1: "))

if travel_class == 1:
    rate = 1.5
elif travel_class == 2:
    rate = 2.5
else:
    rate = 4

fare = distance * rate

if age < 5:
    fare = 0
elif age >= 60:
    fare = fare * 0.75

print("Final Fare =", fare)