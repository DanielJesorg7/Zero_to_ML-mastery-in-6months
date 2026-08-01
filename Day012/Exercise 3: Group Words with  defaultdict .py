from collections import defaultdict

user_input = input("Enter words separated by spaces: ")
words = user_input.split()

grouped_words = defaultdict(list)
for word in words:
    first_letter = word[0].lower()
    grouped_words[first_letter].append(word)

for letter, word_list in sorted(grouped_words.items()):
    print(f"{letter}: {word_list}")
