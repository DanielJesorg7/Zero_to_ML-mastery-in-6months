import numpy as np
import pandas as pd

# 1. Create the base data
data = {
    'name': [f'Person {i}' for i in range(1, 21)],
    'age': np.random.randint(1, 81, size=20)
}
df = pd.DataFrame(data)

# 2. FIX: Assign the cut results to a new column so it actually saves
df['age_group'] = pd.cut(df["age"], bins=[0, 12, 19, 59, 80], labels=["child", "teen", "adult", "senior"])

# 3. FIX: Add the income column BEFORE trying to use it in qcut
df['Income'] = np.random.randint(100000, 1000001, size=20)

# 4. FIX: Use 'Income' instead of 'salary' (since 'salary' doesn't exist)
df['salary_tier'] = pd.qcut(df["Income"], q=4, labels=["low", "mid", "high", "premium"])

# 5. Create your 5-bucket income quintile
df['income_quintile'] = pd.qcut(df['Income'], q=5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

# Print results
print("--- Updated DataFrame ---")
print(df.to_string(index=False))

print("\n--- Value Counts for income_quintile ---")
# FIX: Added () to make the function actually execute
print(df['income_quintile'].value_counts()) 
