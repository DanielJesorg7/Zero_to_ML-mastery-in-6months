import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "city": ["Lagos", "Abuja", "Lagos", "Kano"],
    "department": ["Engineering", "Sales", "Engineering", "HR"]
}

df = pd.DataFrame(data)

# FIX: Assign the result back to df, and do both columns at once
df = pd.get_dummies(df, columns=["city", "department"])

print(df)
