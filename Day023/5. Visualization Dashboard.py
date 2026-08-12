import pandas as pd
import matplotlib.pyplot as plt

print("--- EXERCISE 5: VISUALIZATION DASHBOARD ---")

# Setup: Load engineered structural data structures
try:
    df_eng = pd.read_csv("sales_data_engineered.csv", parse_dates=['date'], index_col='date')
except FileNotFoundError:
    print("Error: 'sales_data_engineered.csv' missing. Run Exercise 3 script first.")
    exit()

# Set up matplotlib native canvas dimensions layout
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# 1. Top-left: Bar chart of total revenue by region
region_rev = df_eng.groupby('region')['revenue'].sum()
axes[0, 0].bar(region_rev.index, region_rev.values, color='steelblue', edgecolor='black')
axes[0, 0].set_title("Total Revenue by Region")
axes[0, 0].set_xlabel("Region")
axes[0, 0].set_ylabel("Total Revenue")

# 2. Top-right: Line plot of daily revenue
daily_rev = df_eng['revenue'].resample('D').sum()
axes[0, 1].plot(daily_rev.index, daily_rev.values, color='firebrick', linewidth=1.5)
axes[0, 1].set_title("Daily Revenue Profile")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Revenue")
axes[0, 1].tick_params(axis='x', rotation=30)

# 3. Bottom-left: Histogram of customer_rating
ratings_clean = df_eng['customer_rating'].dropna()
axes[1, 0].hist(ratings_clean, bins=5, color='darkseagreen', edgecolor='black', rwidth=0.85)
axes[1, 0].set_title("Distribution of Customer Ratings")
axes[1, 0].set_xlabel("Rating Scale")
axes[1, 0].set_ylabel("Counts")

# 4. Bottom-right: Scatter plot of price_per_unit vs units_sold
axes[1, 1].scatter(df_eng['price_per_unit'], df_eng['units_sold'], color='indigo', alpha=0.5)
axes[1, 1].set_title("Price per Unit vs Units Sold")
axes[1, 1].set_xlabel("Price Per Unit")
axes[1, 1].set_ylabel("Units Sold")

# Apply dynamic tight alignment spacing layouts and save execution output artifact
plt.tight_layout()
plt.savefig("eda_dashboard.png")
plt.close()
print("Successfully generated and saved asset to disk as 'eda_dashboard.png'")
