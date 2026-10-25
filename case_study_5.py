# Case Study 5 : Retail Billing with Discount Rules
total = 0

for i in range(1, 4):
    price = float(input(f"Enter price of item {i}: "))
    qty = int(input(f"Enter quantity of item {i}: "))
    total += price * qty

member = input("Premium member (yes/no): ")

discount = 0

if total >= 5000:
    discount += total * 0.05

if member.lower() == "yes":
    discount += total * 0.10

net = total - discount

print("Total Bill =", total)
print("Discount =", discount)
print("Net Amount =", net)