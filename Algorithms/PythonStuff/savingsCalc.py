print("Saving Calculator\n")
name = input("Name: ")

initialBalance = float(input("What is your Initial Balance? "))
desiredBalance = float(input("What is your Desired Balance? "))
months = int(input("In what amount of months do you wish to achieve your Desired Balance: "))

savings = (desiredBalance - initialBalance) / months

print(f"{name}, in order to achieve a desired balance of ${round(desiredBalance, 0)} you need to save ${round(savings, 0)} for {months} months")

