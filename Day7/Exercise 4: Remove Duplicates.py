user_input = input("Enter words: ")
words = user_input.split()

unique_list = []

# Loop to check and preserve original order
for word in words:
    if word not in unique_list:
        unique_list.append(word)

print(f"Unique: {unique_list}")
