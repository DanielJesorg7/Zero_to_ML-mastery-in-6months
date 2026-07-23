sentence = input("Enter a sentence: ")

print(f"Total chars (with spaces): {len(sentence)}")
print(f"Total chars (no spaces): {len(sentence.replace(' ', ''))}")
print(f"Word count: {len(sentence.split())}")
print(f"Title Case: {sentence.title()}")
