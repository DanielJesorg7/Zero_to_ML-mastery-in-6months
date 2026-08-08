import numpy as np  # FIX 1: Import numpy so np.where works
import pandas as pd

data = {
    "full_name": ["  adeleke jesorg  ", "DANIEL ORIOLA", "  sarah smith  "],
    "email": ["Adeleke@GMAIL.com", "daniel@Yahoo.com", "SARAH@Hotmail.COM"],
    "salary": [500000, 750000, 600000]
}
df = pd.DataFrame(data)

# FIX 2: Chain .strip() and .title() together on the correct "full_name" column
df["full_name"] = df["full_name"].str.strip().str.title()           

df["email"] = df["email"].str.lower()           
df["domain"] = df["email"].str.split("@").str[1]

# This now runs cleanly because 'np' was imported
df["salary_category"] = np.where(df["salary"] >= 700000, "high", "standard")

print("=== Final Cleaned DataFrame ===")
print(df)
