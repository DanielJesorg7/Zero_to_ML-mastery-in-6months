import pandas as pd
import numpy as np

data = {
    "name": ["Adeleke", "Daniel", "Sarah", "John"],
    "age": [25, 17, 30, 16],
    "income": [500000, 0, 800000, 0]
}

df = pd.DataFrame(data)

def categorize_row(row):
    if row["age"] < 18:
        return "minor"
    elif row["income"] > 600000:
        return "wealthy"
    else:
        return "standard"

df["category"] = df.apply(categorize_row, axis=1)
print(df["category"])