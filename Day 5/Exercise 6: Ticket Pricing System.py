def calculate_ticket_price():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a number for age.")
        return

    day = input("Enter the day of the week (e.g., Saturday): ").strip().lower()
    has_student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == "yes"

    base_price = 5000
    applied_discount_name = "None"
    discount_amount = 0

    discounts = {}
    
    if age < 12:
        discounts["Children (under 12)"] = 0.50
    if age >= 65:
        discounts["Seniors (65+)"] = 0.30
    if has_student_id:
        discounts["Students (any age, with ID)"] = 0.20

    if discounts:
        applied_discount_name = max(discounts, key=discounts.get)
        discount_rate = discounts[applied_discount_name]
        discount_amount = base_price * discount_rate

    price_after_discount = base_price - discount_amount

    surcharge = 0
    is_weekend = day in ["saturday", "sunday"]
    if is_weekend:
        surcharge = 1000

    final_price = price_after_discount + surcharge

    print("\n" + "="*30)
    print("      TICKET PRICE BREAKDOWN      ")
    print("="*30)
    print(f"Base Price:            ₦{base_price}")
    print(f"Applied Discount:      {applied_discount_name}")
    if discount_amount > 0:
        print(f"Discount Saved:       -₦{int(discount_amount)}")
    print(f"Price After Discount:  ₦{int(price_after_discount)}")
    if is_weekend:
        print(f"Weekend Surcharge:    +₦{surcharge} ({day.capitalize()})")
    print("-"*30)
    print(f"FINAL TICKET PRICE:    ₦{int(final_price)}")
    print("="*30)

calculate_ticket_price()
