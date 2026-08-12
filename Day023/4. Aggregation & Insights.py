import pandas as pd

print("--- EXERCISE 4: AGGREGATION & INSIGHTS ---")

# Setup: Load engineered baseline structural table
try:
    df_eng = pd.read_csv("sales_data_engineered.csv", parse_dates=['date'], index_col='date')
except FileNotFoundError:
    print("Error: 'sales_data_engineered.csv' missing. Run Exercise 3 script first.")
    exit()

# 1. Total revenue by region
print("### Total revenue by region ###")
print(df_eng.groupby('region')['revenue'].sum())
print("\n")

# 2. Average customer_rating by product
print("### Average customer_rating by product ###")
print(df_eng.groupby('product')['customer_rating'].mean())
print("\n")

# 3. Best selling product by units_sold (sum)
print("### Best selling product by units_sold (sum) ###")
best_prod = df_eng.groupby('product')['units_sold'].sum().idxmax()
best_val = df_eng.groupby('product')['units_sold'].sum().max()
print(f"Product: {best_prod} | Total Units Sold: {best_val}\n")

# 4. Worst performing region by revenue
print("### Worst performing region by revenue ###")
worst_region = df_eng.groupby('region')['revenue'].sum().idxmin()
worst_val = df_eng.groupby('region')['revenue'].sum().min()
print(f"Region: {worst_region} | Total Revenue: {worst_val}\n")

# 5. Weekend vs weekday average revenue
print("### Weekend vs weekday average revenue ###")
print(df_eng.groupby('is_weekend')['revenue'].mean())
