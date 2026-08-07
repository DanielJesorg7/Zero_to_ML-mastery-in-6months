import pandas as pd

# Create a DataFrame with 6 rows of sales data
sales_data = {
    "date": ["2026-08-01", "2026-08-01", "2026-08-02", "2026-08-02", "2026-08-03", "2026-08-03"],
    "product": ["Laptop", "Phone", "Laptop", "Monitor", "Phone", "Monitor"],
    "region": ["Lagos", "Abuja", "Lagos", "Kano", "Abuja", "Lagos"],
    "amount": [500000, 200000, 500000, 80000, 400000, 160000]
}
df_sales = pd.DataFrame(sales_data)

# Total sales by product
product_sales = df_sales.groupby("product")["amount"].agg("sum")
print("--- Total Sales by Product ---")
print(product_sales)

# Total sales by region
region_sales = df_sales.groupby("region")["amount"].agg("sum")
print("\n--- Total Sales by Region ---")
print(region_sales)

# Best selling product (highest total amount)
best_selling = product_sales.idxmax()
print(f"\n--- Best Selling Product ---\n{best_selling} (Total: {product_sales.max()})")

# Average sale amount
avg_sale = df_sales["amount"].mean()
print(f"\n--- Average Sale Amount ---\n{avg_sale:.2f}")
