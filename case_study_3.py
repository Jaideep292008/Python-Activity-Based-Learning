# Case Study 3: Multi-Plan Telecommunications Cost Optimization
usage = float(input("Enter data usage (GB): "))

planA = 199 + max(0, usage - 2) * 50
planB = 299 + max(0, usage - 5) * 30
planC = 399 + max(0, usage - 10) * 20

print("Plan A =", planA)
print("Plan B =", planB)
print("Plan C =", planC)

minimum = min(planA, planB, planC)

if minimum == planA:
    print("Best Plan: A")
elif minimum == planB:
    print("Best Plan: B")
else:
    print("Best Plan: C")