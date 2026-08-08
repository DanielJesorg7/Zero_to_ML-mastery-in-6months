import numpy as np
import pandas as pd

data = {
    "product_id": ["101", "102", "103", "104"],
    "price": ["5000.50", "INVALID", "12000", "8000"],
    "quantity": ["10", "5", "N/A", "20"],
    "date": ["2026-08-01", "2026-08-02", "2026-08-03", "2026-08-04"]
}

df = pd.DataFrame(data)

df["product_id"] = df["product_id"].astype(int)

df["price"] = pd.to_numeric(df["price"], errors="coerce")  # invalid → NaN

# 1. Force strings like "N/A" into numeric NaN 
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# 2. Fill the NaN values with 0 and overwrite the column
df["quantity"] = df["quantity"].fillna(0)

# 3. Safely convert to integer now that the text data is gone
df["quantity"] = df["quantity"].astype(int)

print("=== Dtypes BEFORE Datetime Conversion ===")
print(df.dtypes)
print(f"Current 'date' type: {df['date'].dtype}\n")


df["date"] = pd.to_datetime(df["date"])  # string → datetime

print("=== Dtypes AFTER Datetime Conversion ===")
print(df.dtypes)
print(f"New 'date' type: {df['date'].dtype}\n")

print("=== Final DataFrame ===")
print(df)
