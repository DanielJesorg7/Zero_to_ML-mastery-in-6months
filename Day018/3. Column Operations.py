# Using the DataFrame from Exercise 2

# Add a total_value column: price * quantity
df["total_value"] = df["price"] * df["quantity"]

# Add a category column: "electronics" for all rows
df["category"] = "electronics"

# Print only product and total_value columns
print("--- Selected Columns ---")
print(df[["product", "total_value"]])

# Drop the category column
df = df.drop(columns=["category"])
print("\n--- After Dropping Category ---")
print(df)
