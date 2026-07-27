# 1. All numbers from 1 to 50 divisible by 7
divisible_by_7 = [x for x in range(1, 51) if x % 7 == 0]

# 2. All squares of numbers from 1 to 20
squares = [x**2 for x in range(1, 21)]

# 3. All words from a sentence that are longer than 4 characters
sentence = "The quick brown fox jumps over the lazy dog"
long_words = [word for word in sentence.split() if len(word) > 4]

# 4. A list of tuples (number, square) for numbers 1 to 10
number_square_tuples = [(x, x**2) for x in range(1, 11)]

# Print all four results
print("1.", divisible_by_7)
print("2.", squares)
print("3.", long_words)
print("4.", number_square_tuples)
