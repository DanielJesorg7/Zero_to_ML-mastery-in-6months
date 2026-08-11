import pandas as pd
import numpy as np

# Independent Setup (Rebuilding base data)
dates = pd.date_range(start="2026-08-01", end="2026-08-15")
sales = np.random.randint(1000, 10001, size=len(dates))
df = pd.DataFrame({"sales": sales}, index=dates)

# 1. Create a 3_day_avg column
df['3_day_avg'] = df['sales'].rolling(window=3).mean()

# 2. Create a 7_day_avg column
df['7_day_avg'] = df['sales'].rolling(window=7).mean()

# 3. Print the entire DataFrame
print("--- DataFrame with Rolling Averages ---")
print(df)
