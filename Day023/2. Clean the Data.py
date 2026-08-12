import numpy as np
import pandas as pd

print("--- EXERCISE 2: DATA CLEANING ---")

# Setup: Load raw file
try:
    df_loaded = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    print("Error: 'sales_data.csv' missing. Run Exercise 1 script first.")
    exit()

print(f"Shape Before Cleaning: {df_loaded.shape}")

# 1. Convert date to datetime and set as index
df_loaded['date'] = pd.to_datetime(df_loaded['date'])
df_cleaned = df_loaded.set_index('date')

# 2. Fill missing customer_rating with median
median_rating = df_cleaned['customer_rating'].median()
df_cleaned['customer_rating'] = df_cleaned['customer_rating'].fillna(median_rating)

# 3. Create a revenue column
df_cleaned['revenue'] = df_cleaned['units_sold'] * df_cleaned['price_per_unit']

# 4. Remove rows where units_sold <= 0
df_cleaned = df_cleaned[df_cleaned['units_sold'] > 0]

# 5. Print dynamic metrics
print(f"Shape After Cleaning:  {df_cleaned.shape}")

# Save state for the subsequent standalone components
df_cleaned.to_csv("sales_data_cleaned.csv")
