# Case Study 7 : Multi-Currency Travel Budget Analysis
budget = float(input("Budget in INR: "))
expense = float(input("Expense in USD: "))

usd_budget = budget / 83

print("Budget in USD =", round(usd_budget, 2))

if expense <= usd_budget:
    print("Within Budget")
else:
    print("Budget Exceeded")