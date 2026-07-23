first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
birth_year = int(input("Enter your birth year: "))

print("Username Options:")
print(f"Option 1: {first_name}.{last_name}")
print(f"Option 2: {first_name[0]}{last_name}")
print(f"Option 3: {first_name}_{last_name}_{birth_year}")
