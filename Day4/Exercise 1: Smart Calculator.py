num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
difference = num1 - num2
product = num1 * num2
larger = max(num1, num2)
round_num1 = round(num1, 2)
round_num2 = round(num2, 2)

print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")

if num2 != 0:
    division = num1 / num2
    floor_div = num1 // num2
    modulus = num1 % num2
    print(f"Division: {division}")
    print(f"Floor Division: {floor_div}")
    print(f"Modulus: {modulus}")
else:
    print("Division: Cannot divide by zero")
    print("Floor Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")

print(f"Larger number: {larger}")
print(f"Both rounded: {round_num1} and {round_num2}")
