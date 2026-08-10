import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame of 6 months of sales data
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "product_a": [100, 120, 110, 140, 130, 150],
    "product_b": [80, 95, 85, 110, 105, 120],
    "product_c": [45, 60, 55, 70, 65, 80]
}
df = pd.DataFrame(data)

# --- Figure 1: Line Chart for all three products ---
plt.figure(figsize=(7, 4))
plt.plot(df["month"], df["product_a"], marker='o', label="Product A")
plt.plot(df["month"], df["product_b"], marker='s', label="Product B")
plt.plot(df["month"], df["product_c"], marker='^', label="Product C")

plt.title("Product Sales Over 6 Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.savefig("products_line_chart.png")
plt.show()

# --- Figure 2: Stacked Bar Chart of total sales ---
plt.figure(figsize=(7, 4))
plt.bar(df["month"], df["product_a"], label="Product A")
plt.bar(df["month"], df["product_b"], bottom=df["product_a"], label="Product B")
plt.bar(df["month"], df["product_c"], bottom=df["product_a"] + df["product_b"], label="Product C")

plt.title("Total Monthly Sales breakdown")
plt.xlabel("Month")
plt.ylabel("Total Sales Units")
plt.legend()
plt.savefig("sales_stacked_bar.png")
plt.show()
