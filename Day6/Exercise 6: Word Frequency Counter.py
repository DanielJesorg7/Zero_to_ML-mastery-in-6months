sentence = input("Enter a sentence: ")

sentence = sentence.lower()

punctuation_chars = [".", ",", "!", "?", ";", ":"]
for char in punctuation_chars:
    sentence = sentence.replace(char, "")

words = sentence.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in sorted(word_counts.keys()):
    print(f"{word}: {word_counts[word]}")
