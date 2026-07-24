bill_amount = float(input("Bill amount: "))
tip_percentage = float(input("Tip percentage (10, 15, 18, 20, or custom): "))
people = int(input("Number of people: "))

tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount

print(f"\nTip: ${tip_amount:.2f}")
print(f"Total: ${total_bill:.2f}")

if people == 1:
    print("You pay everything!")
else:
    amount_per_person = total_bill / people
    print(f"Each person pays: ${amount_per_person:.2f}")
