# Case Study 1: Progressive Electricity Billing
units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid input")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    total = bill + 50  # Fixed charge
    print("Electricity Bill =", total)