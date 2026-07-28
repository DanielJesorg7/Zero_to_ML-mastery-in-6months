phonebook = {}

while True:
    command = input("Command: ").strip()
    if not command:
        continue
        
    parts = command.split()
    action = parts[0].lower()
    
    if action == "quit":
        print("Exit")
        break
        
    elif action == "add" and len(parts) >= 3:
        name = parts[1]
        number = parts[2]
        phonebook[name] = number
        print(f"Added {name}")
        
    elif action == "search" and len(parts) >= 2:
        name = parts[1]
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Not found")
            
    elif action == "delete" and len(parts) >= 2:
        name = parts[1]
        if name in phonebook:
            del phonebook[name]
            print(f"Removed {name}")
        else:
            print("Not found")
            
    elif action == "show":
        for name in sorted(phonebook.keys()):
            print(f"{name}: {phonebook[name]}")
            
    else:
        print("Invalid command syntax.")
