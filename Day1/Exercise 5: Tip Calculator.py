# Exercise 5: Tip Calculator (FIXED)
bill_amount = float(input("Enter the bill amount: "))
tip = bill_amount * 0.15
total = bill_amount + tip
print(f"Tip: ${tip:.2f}")
print(f"Total bill: ${total:.2f}")
