shopping_list = []

while True:
    action = input("What do you want to do? ").strip()
    
    if action == "done":
        print(f"Final list: {shopping_list}")
        break
    elif action.startswith("add "):
        item = action[4:]
        shopping_list.append(item)
    elif action.startswith("remove "):
        item = action[7:]
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"'{item}' not found in the list.")
    elif action == "show":
        print(shopping_list)
    elif action == "clear":
        shopping_list.clear()
    else:
        print("Invalid command. Use add [item], remove [item], show, clear, or done.")
