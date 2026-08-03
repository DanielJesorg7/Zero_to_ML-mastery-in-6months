import json
import datetime

FILENAME = "expenses.json"
expenses = []

def load_from_json():
    global expenses
    try:
        with open(FILENAME, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def save_to_json():
    try:
        with open(FILENAME, "w") as file:
            json.dump(expenses, file, indent=4)
        print("Data saved to JSON successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def add_expense():
    category = input("Enter category (e.g., Food, Transport): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date_str:
        date_str = str(datetime.date.today())
        
    expenses.append({"category": category, "amount": amount, "date": date_str})
    print("Expense added.")

def view_all_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. [{exp['date']}] {exp['category']}: ${exp['amount']:.2f}")

def view_total_by_category():
    totals = {}
    for exp in expenses:
        cat = exp['category']
        totals[cat] = totals.get(cat, 0) + exp['amount']
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")

def view_monthly_total():
    month_input = input("Enter month (YYYY-MM): ").strip()
    total = sum(exp['amount'] for exp in expenses if exp['date'].startswith(month_input))
    print(f"Total for {month_input}: ${total:.2f}")

# Main loop execution interface
load_from_json()
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. View monthly total")
    print("5. Save to JSON")
    print("6. Load from JSON")
    print("7. Exit")
    
    choice = input("Select an option (1-7): ").strip()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        view_total_by_category()
    elif choice == "4":
        view_monthly_total()
    elif choice == "5":
        save_to_json()
    elif choice == "6":
        load_from_json()
        print("Loaded data from JSON file.")
    elif choice == "7":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid option. Please try again.")
