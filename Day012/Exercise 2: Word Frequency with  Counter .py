from collections import Counter

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_counts = Counter(words)

print("\n3 most common words:")
for word, count in word_counts.most_common(3):
    print(f"{word}: {count}")
