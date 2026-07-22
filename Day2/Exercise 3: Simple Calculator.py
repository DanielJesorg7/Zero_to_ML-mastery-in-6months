num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Calculating...")
print("---------------------")

total = num1 + num2
difference = num1 - num2
product = num1 * num2

if num2 != 0:
    division = num1 / num2
    print(f"Sum: {total}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Division: {division:.2f}")
else:
    print(f"Sum: {total}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print("Division: Cannot divide by zero!")
