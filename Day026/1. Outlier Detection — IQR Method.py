import numpy as np
import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E", "F", "G"],
    "salary": [300000, 350000, 320000, 400000, 310000, 1200000, 290000]
}


df = pd.DataFrame(data)

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["salary"] < lower) | (df["salary"] > upper)]
print(outliers)