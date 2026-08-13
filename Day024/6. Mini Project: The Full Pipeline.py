import io
import pandas as pd

# 1. Define the full data pipeline function
def analyze_sales(csv_file):
    # Reads a CSV with columns: date, product, region, amount
    df = pd.read_csv(csv_file)

    # Converts date to datetime and sets as index
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # Fills any missing amount with 0
    df["amount"] = df["amount"].fillna(0)

    # Calculate metrics for the return dictionary
    total_revenue = df["amount"].sum()
    best_product = df.groupby("product")["amount"].sum().idxmax()
    best_region = df.groupby("region")["amount"].sum().idxmax()
    monthly_revenue = df["amount"].resample("M").sum()

    return {
        "total_revenue": total_revenue,
        "best_product": best_product,
        "best_region": best_region,
        "monthly_revenue": monthly_revenue,
    }


# 2. Create a test CSV in-code with 10 rows (includes sample missing values)
test_csv_data = """date,product,region,amount
2026-01-05,Laptop,North,1200
2026-01-15,Phone,South,800
2026-01-20,Laptop,East,1200
2026-02-02,Tablet,North,
2026-02-14,Phone,West,800
2026-02-28,Laptop,West,2400
2026-03-05,Tablet,South,400
2026-03-12,Phone,North,800
2026-03-22,Laptop,East,1200
2026-03-29,Tablet,West,400
"""

# Call the function using string input simulation and print the final metrics summary
results = analyze_sales(io.StringIO(test_csv_data))

print("--- PIPELINE RESULTS ---")
print(f"Total Revenue: {results['total_revenue']}")
print(f"Best Product:  {results['best_product']}")
print(f"Best Region:   {results['best_region']}")
print("\nMonthly Revenue Series:")
print(results["monthly_revenue"])
