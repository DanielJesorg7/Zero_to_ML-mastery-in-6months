import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ").strip().lower()

if user_choice not in choices:
    print("Invalid choice! Please restart and pick rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("Result: It's a tie!")
        print(f"Both players picked {user_choice}.")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Result: You won!")
            print("Reason: Rock beats scissors!")
        else:
            print("Result: Computer won!")
            print("Reason: Paper beats rock!")

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Result: You won!")
            print("Reason: Paper beats rock!")
        else:
            print("Result: Computer won!")
            print("Reason: Scissors beats paper!")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Result: You won!")
            print("Reason: Scissors beats paper!")
        else:
            print("Result: Computer won!")
            print("Reason: Rock beats scissors!")
