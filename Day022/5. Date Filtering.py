import pandas as pd
import numpy as np

# 1. Create a DataFrame with 30 days of data (August 2026)
aug_dates = pd.date_range(start="2026-08-01", periods=30)
aug_sales = np.random.randint(1000, 10001, size=30)
df_aug = pd.DataFrame({"sales": aug_sales}, index=aug_dates)

# 2. Filter and print only weekdays (Monday-Friday)
weekdays_df = df_aug[df_aug.index.dayofweek < 5]
print("--- Weekdays Only ---")
print(weekdays_df.head(5))

# 3. Filter and print only dates where sales > 5000
high_sales_df = df_aug[df_aug['sales'] > 5000]
print("\n--- Sales > 5000 ---")
print(high_sales_df.head(5))

# 4. Print the sum of sales for the first week (Aug 1-7)
first_week_sum = df_aug.loc["2026-08-01":"2026-08-07", "sales"].sum()
print(f"\nSum of First Week Sales: {first_week_sum}")
