import pandas as pd

sales = pd.DataFrame({
    "date": ["2026-08-01", "2026-08-01", "2026-08-02", "2026-08-02", "2026-08-03"],
    "product": ["Laptop", "Phone", "Laptop", "Monitor", "Phone"],
    "region": ["Lagos", "Lagos", "Abuja", "Kano", "Abuja"],
    "amount": [500000, 200000, 450000, 80000, 180000]
})

# Group by region, then aggregate amount in 3 ways
# agg() takes a dictionary: {column: [functions]}
result = sales.groupby("region")["amount"].agg(["sum", "mean", "count"])

# Rename columns for clarity
result.columns = ["total_revenue", "avg_sale", "num_transactions"]

print(result)
