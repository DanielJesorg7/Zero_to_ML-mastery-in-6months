import numpy as np
import pandas as pd

print("--- EXERCISE 1: GENERATE & INSPECT ---")

# 1. Generate Dataset
np.random.seed(42)
n = 200

data = {
    "date": pd.date_range("2026-01-01", periods=n, freq="D"),
    "product": np.random.choice(["Laptop", "Phone", "Tablet"], size=n),
    "region": np.random.choice(["Lagos", "Abuja", "Kano"], size=n),
    "units_sold": np.random.randint(-1, 15, size=n),  # Includes negatives to mimic real-world cleaning scenarios
    "price_per_unit": np.random.randint(10000, 350000, size=n),
    "customer_rating": np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0, np.nan], size=n, p=[0.1, 0.1, 0.2, 0.3, 0.2, 0.1])
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print("Saved raw data to 'sales_data.csv'\n")

# 2. Inspect Program
df_loaded = pd.read_csv("sales_data.csv")

print("[Shape]:")
print(df_loaded.shape)

print("\n[Data Types]:")
print(df_loaded.dtypes)

print("\n[Head(10)]:")
print(df_loaded.head(10))

print("\n[Description for Numeric Columns]:")
print(df_loaded.describe())

print("\n[Count of Missing Values per Column]:")
print(df_loaded.isnull().sum())
