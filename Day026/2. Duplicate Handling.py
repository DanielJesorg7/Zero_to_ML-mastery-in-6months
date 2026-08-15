import pandas as pd

data = {
    "name": ["Adeleke", "Daniel", "Adeleke", "Sarah", "Daniel", "John"],
    "age": [25, 22, 25, 24, 22, 30],
    "city": ["Lagos", "Abuja", "Lagos", "Kano", "Abuja", "Lagos"]
}

df = pd.DataFrame(data)

print("Shape BEFORE:", df.shape)
print("\nDuplicate mask:")
print(df.duplicated())
print("\nNumber of duplicates:", df.duplicated().sum())

# Print only the rows that ARE duplicates (not the first occurrence)
print("\nDuplicate rows only:")
print(df[df.duplicated()])

# FIX: Assign the result back to df
df = df.drop_duplicates(keep="first")

print("\nShape AFTER dropping duplicates:", df.shape)
print(df)
