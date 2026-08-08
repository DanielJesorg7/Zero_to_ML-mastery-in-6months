import numpy as np
import pandas as pd

# --- Step 0: Create the messy_data.csv file manually in code ---
messy_csv_content = """name,age,income,city
Adeleke,25,500000,Lagos
Daniel,,INVALID,Abuja
Sarah,24,,Kano
John ,22,300000,lagos
MARY,30,450000,ABUJA
,,,"""

with open("messy_data.csv", "w", encoding="utf-8") as file:
    file.write(messy_csv_content)


# --- Complete Cleaning Pipeline ---

# 1. Read the CSV
df_messy = pd.read_csv("messy_data.csv")
orig_shape = df_messy.shape

# 2. Drop rows where ALL values are missing
df_clean = df_messy.dropna(how="all").copy()

# 3. Strip whitespace from name and convert to Title Case
df_clean["name"] = df_clean["name"].str.strip().str.title()

# 4. Convert city to Title Case
df_clean["city"] = df_clean["city"].str.strip().str.title()

# 5. Fill missing age with median
df_clean["age"] = pd.to_numeric(df_clean["age"], errors="coerce")
df_clean["age"] = df_clean["age"].fillna(df_clean["age"].median())

# 6. Convert income to numeric (invalid -> NaN), then fill NaN with mean income
df_clean["income"] = pd.to_numeric(df_clean["income"], errors="coerce")
df_clean["income"] = df_clean["income"].fillna(df_clean["income"].mean())

# 7. Add income_bracket column ("low" < 400000, "medium" 400000-600000, "high" > 600000)
# pd.cut automatically buckets continuous numerical ranges cleanly
bins = [0, 399999, 600000, float("inf")]
labels = ["low", "medium", "high"]
df_clean["income_bracket"] = pd.cut(df_clean["income"], bins=bins, labels=labels)

# 8. Save cleaned data to cleaned_data.csv
df_clean.to_csv("cleaned_data.csv", index=False)

# 9. Print summary
print("=== Data Cleaning Summary ===")
print(f"Original Shape: {orig_shape}")
print(f"Cleaned Shape : {df_clean.shape}")
print("\nMissing Values Count After Cleaning:")
print(df_clean.isnull().sum())

print("\n=== Final Cleaned DataFrame Layout ===")
print(df_clean)
