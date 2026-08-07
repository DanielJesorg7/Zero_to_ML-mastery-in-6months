import pandas as pd

data = {
    "name": ["Adeleke", "Daniel", "Sarah", "John", "Mary"],
    "math": [85, 90, 72, 60, 95],
    "english": [78, 82, 95, 55, 92],
    "physics": [90, 88, 85, 70, 98]
}
df = pd.DataFrame(data)

df["average"] = df[["math", "english", "physics"]].mean(axis=1)

print("--- Sorted by Average ---")
df_sorted = df.sort_values(by="average", ascending=False)
print(df_sorted)

print("\n--- Top 2 Students ---")
print(df_sorted.head(2))

print("\n--- Highest Math Score ---")
print(df.loc[[df["math"].idxmax()]])
