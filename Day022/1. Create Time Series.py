import pandas as pd
import numpy as np

# 1. Create date range and random sales data
dates = pd.date_range(start="2026-08-01", end="2026-08-15")
sales = np.random.randint(1000, 10001, size=len(dates))

# 2. Build the DataFrame with date as index
df = pd.DataFrame({"sales": sales}, index=dates)

# 3. Print first and last 5 rows
print("--- First 5 Rows ---")
print(df.head(5))

print("\n--- Last 5 Rows ---")
print(df.tail(5))
