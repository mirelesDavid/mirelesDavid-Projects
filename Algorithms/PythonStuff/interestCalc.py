print("***Welcome to the Interest Calculator***")

interestRate = 0.08
accumulatedInterest = 0
name = input("Enter your name: ")
initialBalance = int(input("Enter your initial balance: "))
depositAmount = int(input("Enter the deposit amount for October: "))
withdrawalAmount = int(input("Enter the withdrawal amount for December: "))

for month in range(1, 12 + 1):
    monthlyInterest = initialBalance * interestRate / 12
    accumulatedInterest += monthlyInterest
    initialBalance += monthlyInterest

    if month == 10:
        initialBalance += depositAmount

    if month == 12:
        initialBalance -= withdrawalAmount

    print(f"The balance for month {month} is ${round(initialBalance, 0)}")

print(f"The end-of-year balance in the investment account will be: ${round(initialBalance, 0)}")
print(f"The interest earned in a year will be: ${round(accumulatedInterest, 0)}")


