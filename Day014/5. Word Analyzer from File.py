from collections import Counter
import string

try:
    with open("article.txt", "r") as file:
        text = file.read()

    # Clean punctuation and split into lowercase words
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()

    if not words:
        print("The file is empty.")
    else:
        total_words = len(words)
        avg_length = sum(len(word) for word in words) / total_words
        
        counter = Counter(words)
        common_words = counter.most_common(5)
        
        longest_word = max(words, key=len)

        print(f"Total words: {total_words}")
        print(f"Average word length: {avg_length:.2f}")
        print("5 most common words:")
        for word, count in common_words:
            print(f"  - {word}: {count}")
        print(f"Longest word: {longest_word}")

except FileNotFoundError:
    print("Error: 'article.txt' was not found. Please create the file and try again.")
