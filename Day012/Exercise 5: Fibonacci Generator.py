def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Testing by iterating through and printing each value
n_terms = int(input("Enter the number of Fibonacci terms to generate: "))
print(f"The first {n_terms} Fibonacci numbers are:")
for num in fibonacci(n_terms):
    print(num, end=" ")
print()
