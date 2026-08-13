import pandas as pd
import numpy as np

data = {
    "name": ["  adeleke  ", "DANIEL", "  sarah  ", "john", None],
    "age": ["25", "thirty", "24", "22", "28"],
    "salary": [500000, 600000, None, 450000, 700000],
    "department": ["Engineering", "engineering", "  Sales  ", "sales", "Engineering"]
}

# Create the DataFrame
df = pd.DataFrame(data)
print("--- Raw DataFrame ---")
print(df)

# Clean up departments so "Engineering" and "engineering" match perfectly
df['department'] = df['department'].str.strip().str.capitalize()

# Clean up names and handle the missing value safely
df['name'] = df['name'].str.strip().str.capitalize()
# Replace text numbers with digits, then convert the whole column to numeric
df['age'] = df['age'].replace('thirty', '30').astype(int)

# Fill missing values with the average salary
df['salary'] = df['salary'].fillna(df['salary'].mean())

df.dropna(subset=['name'], inplace=True)

