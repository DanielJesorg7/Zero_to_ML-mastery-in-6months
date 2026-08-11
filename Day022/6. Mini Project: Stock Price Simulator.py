import pandas as pd
import numpy as np

# 1. Create a DataFrame simulating 30 days of stock prices
dates = pd.date_range("2026-08-01", periods=30)
prices = 100 + np.cumsum(np.random.normal(0, 2, 30))
volume = np.random.randint(1000000, 5000000, size=30)

stock_df = pd.DataFrame({"price": prices, "volume": volume}, index=dates)

# 2. Calculate daily price change
stock_df['daily_change'] = stock_df['price'] - stock_df['price'].shift(1)

# 3. Calculate 5-day moving average of price
stock_df['5_day_ma'] = stock_df['price'].rolling(window=5).mean()

# 4. Filter days where volume > 3,000,000
high_volume_df = stock_df[stock_df['volume'] > 3000000]
print("--- High Volume Days ---")
print(high_volume_df.head(5))

# 5. Calculate total return
first_price = stock_df['price'].iloc[0]
last_price = stock_df['price'].iloc[-1]
total_return = ((last_price - first_price) / first_price) * 100
print(f"\nTotal Stock Return: {total_return:.2f}%")
