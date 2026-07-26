attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Create a password: ")
    errors = []

    if len(password) < 8:
        errors.append("Must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        errors.append("Must contain at least one digit.")

    if not errors:
        print("Password accepted")
        break
    else:
        print("Invalid password. Reasons:")
        for error in errors:
            print(f"- {error}")
        attempts += 1
        print(f"Attempts remaining: {max_attempts - attempts}\n")

if attempts == max_attempts:
    print("Account locked")
