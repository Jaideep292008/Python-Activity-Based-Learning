# Case Study 8 : Campus Event Financial Planning
tickets = int(input("Tickets Sold: "))
price = float(input("Ticket Price: "))
sponsor = float(input("Sponsorship Amount: "))
expenses = float(input("Expenses: "))

revenue = tickets * price + sponsor
net = revenue - expenses

print("Revenue =", revenue)

if net > 0:
    print("Profit =", net)
elif net < 0:
    print("Loss =", abs(net))
else:
    print("Break Even")