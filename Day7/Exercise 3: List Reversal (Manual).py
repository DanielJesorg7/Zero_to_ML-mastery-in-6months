# Get a list of numbers from space-separated input
user_input = input("Enter numbers: ")
numbers = user_input.split()

reversed_numbers = []

# Manually reverse using a loop
for i in range(len(numbers) - 1, -1, -1):
    # Convert back to integers if needed for exact formatting matching the example
    reversed_numbers.append(int(numbers[i]))

print(f"Reversed: {reversed_numbers}")
