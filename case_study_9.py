# Case Study 9 : ATM Transaction Sequence Simulation
balance = 1000

deposit = int(input("Enter deposit amount: "))
withdraw = int(input("Enter withdrawal amount: "))

balance = balance + deposit

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

print("Final Balance =", balance)