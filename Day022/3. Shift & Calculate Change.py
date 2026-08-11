import pandas as pd
import numpy as np

# Independent Setup (Rebuilding base data)
dates = pd.date_range(start="2026-08-01", end="2026-08-15")
sales = np.random.randint(1000, 10001, size=len(dates))
df = pd.DataFrame({"sales": sales}, index=dates)

# 1. Create previous_day column using .shift(1)
df['previous_day'] = df['sales'].shift(1)

# 2. Create daily_change column
df['daily_change'] = df['sales'] - df['previous_day']

# 3. Filter and print rows where daily_change was positive
positive_change_df = df[df['daily_change'] > 0]
print("--- Rows with Positive Change ---")
print(positive_change_df)
