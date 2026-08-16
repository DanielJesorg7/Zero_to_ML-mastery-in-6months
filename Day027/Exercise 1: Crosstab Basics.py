import pandas as pd

data = {
    "gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "department": ["Eng", "Sales", "Eng", "HR", "Sales", "Eng", "HR", "Sales"],
    "salary": [500000, 400000, 600000, 350000, 450000, 550000, 380000, 420000]
}
df = pd.DataFrame(data)

# Counts
print("--- Counts ---")
print(pd.crosstab(df["gender"], df["department"]))

# With margins (totals)
print("\n--- With Margins ---")
print(pd.crosstab(df["gender"], df["department"], margins=True))

# Average salary by gender and department
print("\n--- Average Salary ---")
print(pd.crosstab(df["gender"], df["department"], values=df["salary"], aggfunc="mean"))
