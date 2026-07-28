products = [("Laptop", 500000), ("Phone", 150000), ("Tablet", 250000)]

# Use loop with tuple unpacking to print
for name, price in products:
    print(f"Product: {name}, Price: ₦{price}")

# Ask user for a budget and print affordable products
budget = float(input("\nEnter your budget: ₦"))
print("Products you can afford:")
for name, price in products:
    if price <= budget:
        print(f"- {name} (₦{price})")
