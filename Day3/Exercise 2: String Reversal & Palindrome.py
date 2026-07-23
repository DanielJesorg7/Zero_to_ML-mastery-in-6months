word = input("Enter word: ")
word_lower = word.lower()
reversed_word = word_lower[::-1]
print (f"Word : {word} \n Reversed : {reversed_word}")
if word_lower == reversed_word :
    print ("Its a palindrome word")
else:
    print ("Its not a palindrome word")