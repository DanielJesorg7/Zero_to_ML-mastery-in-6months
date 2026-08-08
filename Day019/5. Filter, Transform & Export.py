import pandas as pd

# 1. Create lists of data directly
dates = ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04", "2026-08-05", "2026-08-06"]
products = ["Laptop", "Mouse", "Monitor", "Keyboard", "Desk", "Chair"]
regions = ["North", "South", "East", "West", "North", "East"]
amounts = [150000, 20000, 120000, 8000, 110000, 50000]
discounts = [15000, 2000, 5000, 1000, 10000, 5000]

# 2. Build the sales dictionary safely
sales_data = {
    "date": dates,
    "product": products,
    "region": regions,
    "amount": amounts,
    "discount": discounts
}
df_sales = pd.DataFrame(sales_data)

# 3. Filter only rows where amount > 100000
df_filtered = df_sales[df_sales["amount"] > 100000].copy()

# 4. Create final_amount column = amount - discount
df_filtered["final_amount"] = df_filtered["amount"] - df_filtered["discount"]

# 5. Sort by final_amount descending
df_filtered = df_filtered.sort_values(by="final_amount", ascending=False)

# 6. Save the result to filtered_sales.csv (without index)
df_filtered.to_csv("filtered_sales.csv", index=False)

# 7. Read the saved file back and print to confirm
df_confirm = pd.read_csv("filtered_sales.csv")
print("=== Confirmed Saved Sales Data ===")
print(df_confirm)
