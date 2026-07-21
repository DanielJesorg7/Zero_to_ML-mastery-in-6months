num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("calculating")
print("---------------------")
sum = num1+num2
difference = num1 - num2
#  if difference <0:
#      difference = num2-num1
#  else:
 #     return difference
product = num1*num2
quotient = num1 / num2
remainder = num1 % num2

print(f"Sum is {sum} , difference is {difference}, product is {product} , quotient is {quotient:.2f} ,remainder is {remainder}  ")
