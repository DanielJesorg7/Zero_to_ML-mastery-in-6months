import math

r = float(input("Enter radius: "))
d = r * 2
c = 2 * math.pi * r
a = math.pi * r ** 2

print(f"Diameter: {d:.2f}")
print(f"Circumference: {c:.2f}")
print(f"Area: {a:.2f}")
