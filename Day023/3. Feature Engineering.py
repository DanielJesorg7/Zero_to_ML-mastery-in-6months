import pandas as pd

print("--- EXERCISE 3: FEATURE ENGINEERING ---")

# Setup: Load cleaned file and parse its index as a time element
try:
    df_cleaned = pd.read_csv("sales_data_cleaned.csv", parse_dates=['date'], index_col='date')
except FileNotFoundError:
    print("Error: 'sales_data_cleaned.csv' missing. Run Exercise 2 script first.")
    exit()

# 1. Create day_of_week column
df_cleaned['day_of_week'] = df_cleaned.index.day_name()

# 2. Create is_weekend column
df_cleaned['is_weekend'] = df_cleaned['day_of_week'].isin(['Saturday', 'Sunday'])

# 3. Create price_category column
bins = [0, 100000, 250000, float('inf')]
labels = ["budget", "mid", "premium"]
df_cleaned['price_category'] = pd.cut(df_cleaned['price_per_unit'], bins=bins, labels=labels)

# 4. Create revenue_per_unit column
df_cleaned['revenue_per_unit'] = df_cleaned['revenue'] / df_cleaned['units_sold']

# 5. Print head showing new features explicitly
target_cols = ['day_of_week', 'is_weekend', 'price_category', 'revenue_per_unit']
print(df_cleaned[target_cols].head())

# Save current engineered state
df_cleaned.to_csv("sales_data_engineered.csv")
