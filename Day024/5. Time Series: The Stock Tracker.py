import numpy as np
import pandas as pd

# 1. Create a date range of 30 days starting from 2026-08-01
dates = pd.date_range(start="2026-08-01", periods=30)

# 2. Create a Series of random prices (100 to 200) with that date index
np.random.seed(10)
prices = pd.Series(np.random.randint(100, 201, size=30), index=dates)

# 3. Calculate metrics
# 5-day moving average
moving_avg = prices.rolling(window=5).mean()

# Day with the highest price
highest_price_date = prices.idxmax()
highest_price_value = prices.max()

# Total return from first day to last day
total_return = ((prices.iloc[-1] - prices.iloc[0]) / prices.iloc[0]) * 100

# Print results
print("First 8 rows of Moving Average (showing NaNs):")
print(moving_avg.head(8), "\n")
print(
    f"Highest Price: {highest_price_value} on {highest_price_date.strftime('%Y-%m-%d')}\n"
)
print(f"Total Return: {total_return:.2f}%")
