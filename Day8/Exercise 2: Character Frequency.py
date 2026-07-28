sentence = input("Enter sentence: ").replace(" ", "").lower()
freq = {}

for char in sentence:
    freq[char] = freq.get(char, 0) + 1

for char in sorted(freq.keys()):
    print(f"{char}: {freq[char]}")
