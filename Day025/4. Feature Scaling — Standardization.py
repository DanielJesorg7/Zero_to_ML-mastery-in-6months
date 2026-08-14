import numpy as np
import pandas as pd



data = {
    "student": [f"Student_{i}" for i in range(1, 11)],
    "math_score": np.random.randint(40, 100, 10),
    "english_score": np.random.randint(40, 100, 10)
}

df = pd.DataFrame(data)

df["math_standardized"] = (df["math_score"] - df["math_score"].mean()) / df["math_score"].std()

df["english_standardized"] = (df["english_score"] - df["english_score"].mean()) / df["english_score"].std()

print(df["math_standardized"])
print(df["english_standardized"])

#Reason for standardization is because it : Prevents Features with Large Scales from Dominating