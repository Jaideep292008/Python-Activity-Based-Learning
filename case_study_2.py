# Case Study 2: Employee Payroll and Deduction Analysis
basic = float(input("Enter basic salary: "))
overtime_hours = int(input("Enter overtime hours: "))

hra = basic * 0.20
allowance = basic * 0.10
overtime_pay = overtime_hours * 150

gross = basic + hra + allowance + overtime_pay
deduction = gross * 0.08
net = gross - deduction

print("Gross Salary =", gross)
print("Net Salary =", net)