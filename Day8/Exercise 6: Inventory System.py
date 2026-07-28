inventory = {
    "rice": {"quantity": 50, "price": 1200},
    "beans": {"quantity": 30, "price": 1500},
    "garri": {"quantity": 100, "price": 800}
}

while True:
    user_input = input("Enter product name to buy (or type 'done' to finish): ").strip().lower()
    if user_input == "done":
        break
        
    if user_input not in inventory:
        print("Error: Product does not exist!\n")
        continue
        
    try:
        qty_to_buy = int(input(f"Enter quantity of {user_input} to buy: "))
    except ValueError:
        print("Error: Invalid quantity format!\n")
        continue
    
    if qty_to_buy <= 0:
        print("Error: Quantity must be positive!\n")
        continue
        
    available_qty = inventory[user_input]["quantity"]
    if qty_to_buy > available_qty:
        print(f"Error: Quantity unavailable! Only {available_qty} items left.\n")
        continue
        
    unit_price = inventory[user_input]["price"]
    total_cost = unit_price * qty_to_buy
    inventory[user_input]["quantity"] -= qty_to_buy
    
    print("\n--- RECEIPT ---")
    print(f"Product: {user_input.capitalize()}")
    print(f"Quantity: {qty_to_buy}")
    print(f"Unit Price: ₦{unit_price}")
    print(f"Total Cost: ₦{total_cost}")
    print("----------------\n")

print("Thank you for shopping!")
