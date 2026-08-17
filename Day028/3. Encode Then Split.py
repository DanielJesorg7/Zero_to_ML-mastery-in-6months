import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "city": ["Lagos", "Abuja", "Lagos", "Kano", "Abuja", "Lagos", "Kano", "Abuja"],
    "age": [25, 30, 22, 35, 28, 40, 19, 33],
    "income": [500000, 800000, 300000, 900000, 600000, 1000000, 200000, 750000],
    "bought": [0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# Encode BEFORE splitting (prevent data leakage)
df = pd.get_dummies(df, columns=["city"])

X = df.drop("bought", axis=1)
y = df["bought"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train:")
print(X_train)
