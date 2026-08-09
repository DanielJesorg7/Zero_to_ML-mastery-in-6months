import pandas as pd

# --- Create 3 CSV files in code ---
customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Adeleke", "Daniel", "Sarah"],
    "city": ["Lagos", "Abuja", "Kano"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 1, 2, 3],
    "product": ["Laptop", "Phone", "Monitor", "Phone"],
    "amount": [500000, 200000, 80000, 180000]
})

payments = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "status": ["Paid", "Paid", "Unpaid", "Paid"]
})

# Step 1: Merge customers + orders (left join)
# Keep all customers even if they never ordered
step1 = pd.merge(customers, orders, on="customer_id", how="left")

# Step 2: Merge result + payments (left join)
full = pd.merge(step1, payments, on="order_id", how="left")

print("--- Full Merged Data ---")
print(full)

# Step 3: Total revenue per city
city_revenue = full.groupby("city")["amount"].sum()
print("\n--- Total Revenue Per City ---")
print(city_revenue)

# Step 4: Revenue for PAID orders only
paid_only = full[full["status"] == "Paid"]
paid_revenue = paid_only.groupby("city")["amount"].sum()
print("\n--- Paid Revenue Per City ---")
print(paid_revenue)

# Step 5: Top customer by total spending
customer_spending = full.groupby("name")["amount"].sum().sort_values(ascending=False)
print("\n--- Top Customer ---")
print(customer_spending.head(1))
