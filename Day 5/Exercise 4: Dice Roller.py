balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")

if pin != "1234":
    print("Error: Incorrect PIN.")
elif withdrawal <= 0:
    print("Error: Withdrawal amount must be positive.")
elif withdrawal > balance:
    print("Error: Insufficient funds.")
elif withdrawal % 500 != 0:
    print("Error: Amount must be in multiples of 500.")
else:
    new_balance = balance - withdrawal
    print(f"Transaction successful. New balance: {new_balance}")
