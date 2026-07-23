def validate_email():
    email = input("Please enter an email address: ").strip()

    
    if "@" in email:
        print("Check 1: Contains '@' - TRUE")
    else:
        print("Check 1: Contains '@' - FALSE")
        return 

    
    parts = email.split("@", 1)
    domain = parts[1]

    
    if "." in domain:
        print("Check 2: Contains '.' after '@' - TRUE")
    else:
        print("Check 2: Contains '.' after '@' - FALSE")
        return 

    
    if len(domain) >= 3:
        print(f"Check 3: Domain '{domain}' is at least 3 characters - TRUE")
    else:
        print(f"Check 3: Domain '{domain}' is at least 3 characters - FALSE")
        print("Invalid email domain length.")
        return

    print("\nResult: All basic checks passed! This is a valid format.")


validate_email()
