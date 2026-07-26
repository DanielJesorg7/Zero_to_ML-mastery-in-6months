n = int(input("Enter a number n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nThen print the reverse:\n")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
