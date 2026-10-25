# Case Study 10 : Bus Passenger Occupancy Simulation
capacity = 50

boarding = int(input("Passengers boarding: "))
leaving = int(input("Passengers leaving: "))

passengers = boarding - leaving

print("Passengers in Bus =", passengers)

if passengers > capacity:
    print("Bus Capacity Exceeded")
else:
    print("Within Capacity")