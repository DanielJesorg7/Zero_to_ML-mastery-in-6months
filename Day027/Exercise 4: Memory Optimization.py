import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame({
    "id": range(1, 100001),
    "age": np.random.randint(18, 80, 100000),
    "salary": np.random.randint(100000, 1000000, 100000),
    "department": np.random.choice(["Eng", "Sales", "HR", "Finance"], 100000),
    "rating": np.random.choice([1, 2, 3, 4, 5], 100000)
})

print("--- BEFORE ---")
print(df.info(memory_usage="deep"))

# Optimize
df["age"] = df["age"].astype("int8")
df["rating"] = df["rating"].astype("int8")
df["department"] = df["department"].astype("category")

print("\n--- AFTER ---")
print(df.info(memory_usage="deep"))
