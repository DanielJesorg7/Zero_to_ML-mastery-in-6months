import pandas as pd
import numpy as np

# Independent Setup (Rebuilding base data)
dates = pd.date_range(start="2026-08-01", end="2026-08-15")
sales = np.random.randint(1000, 10001, size=len(dates))
df = pd.DataFrame({"sales": sales}, index=dates)

# 1. Resample to weekly ('W') and get the sum
weekly_sum = df.resample('W').sum()
print("--- Weekly Sales Sum ---")
print(weekly_sum)

# 2. Resample to weekly ('W') and get the mean
weekly_mean = df.resample('W').mean()
print("\n--- Weekly Sales Mean ---")
print(weekly_mean)

# 3. Print total sales for the entire period
total_sales = df['sales'].sum()
print(f"\nTotal Sales for Period: {total_sales}")
