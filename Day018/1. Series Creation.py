import pandas as pd
import numpy as np

# Series from list with custom index
s1 = pd.Series([100, 200, 300], index=["jan", "feb", "mar"])
print("Series 1:")
print(s1)
print(f"Dtype: {s1.dtype}\n")

# Series from dict
s2 = pd.Series({"lagos": 15_000_000, "abuja": 3_000_000, "kano": 4_000_000})
print("Series 2:")
print(s2)
print(f"Dtype: {s2.dtype}\n")

# Series from NumPy array
s3 = pd.Series(np.arange(5))
print("Series 3:")
print(s3)
print(f"Dtype: {s3.dtype}")
