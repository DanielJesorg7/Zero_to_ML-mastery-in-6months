import pandas as pd

# Create this DataFrame manually
data = {
    "product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "price": [500000, 200000, 150000, 80000],
    "quantity": [10, 25, 15, 20]
}
df = pd.DataFrame(data)

# Print attributes and methods
print("--- Shape ---")
print(df.shape)

print("\n--- Columns ---")
print(df.columns)

print("\n--- Dtypes ---")
print(df.dtypes)

print("\n--- Head(2) ---")
print(df.head(2))

print("\n--- Describe ---")
print(df.describe())
