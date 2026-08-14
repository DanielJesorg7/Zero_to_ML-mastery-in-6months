import numpy as np
import pandas as pd



data = {
    "student": [f"Student_{i}" for i in range(1, 11)],
    "math_score": np.random.randint(40, 100, 10),
    "english_score": np.random.randint(40, 100, 10)
}

df = pd.DataFrame(data)
df["math_minmax"] = (df["math_score"] - df["math_score"].min()) / (df["math_score"].max() - df["math_score"].min())

df["english_minmax"] = (df["english_score"] - df["english_score"].min()) / (df["english_score"].max() - df["english_score"].min())

print(df["math_minmax"])

print(df["english_minmax"])



