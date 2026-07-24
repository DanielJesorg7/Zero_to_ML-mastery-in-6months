import random

secret_number = random.randint(1, 100)
guesses_remaining = 7
guess_count = 0

print("I'm thinking of a number between 1 and 100. You have 7 guesses.")

while guesses_remaining > 0:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    guesses_remaining -= 1
    
    if guess == secret_number:
        print(f"🎉 Correct! You got it in {guess_count} guesses!")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
        
    if guesses_remaining > 0:
        print(f"Guesses remaining: {guesses_remaining}\n")
    else:
        print(f"😢 Game over! The number was {secret_number}")
