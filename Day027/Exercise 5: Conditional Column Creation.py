import pandas as pd
import numpy as np

data = {
    "employee": ["A", "B", "C", "D", "E"],
    "years": [2, 5, 8, 1, 12],
    "performance": [3.5, 4.2, 2.8, 4.8, 3.9]
}
df = pd.DataFrame(data)

# bonus_eligible: True if years >= 3 AND performance >= 4.0
df["bonus_eligible"] = np.where((df["years"] >= 3) & (df["performance"] >= 4.0), True, False)

# bonus_amount: if eligible, years * performance * 10000, else 0
df["bonus_amount"] = np.where(df["bonus_eligible"], df["years"] * df["performance"] * 10000, 0)

print(df)
