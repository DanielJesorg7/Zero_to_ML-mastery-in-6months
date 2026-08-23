import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)
n = 400

data = {
    "age": np.random.randint(18, 65, n),
    "income": np.random.randint(100000, 2000000, n),
    "purchase_frequency": np.random.randint(1, 50, n),
    "avg_order_value": np.random.randint(5000, 100000, n),
    "website_visits": np.random.randint(5, 200, n)
}
df = pd.DataFrame(data)

df["high_value"] = np.where(
    (df["purchase_frequency"] > 25) & (df["avg_order_value"] > 40000) & (df["website_visits"] > 50),
    1, 0
)

X = df.drop("high_value", axis=1)
y = df["high_value"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# New customer prediction — scale first
new_customer = [[30, 500000, 35, 60000, 80]]
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)
print("High-value prediction (1=yes, 0=no):", prediction)

# Bonus: find optimal K
for k in [1, 3, 5, 7, 10, 15, 20, 30]:
    m = KNeighborsClassifier(n_neighbors=k)
    m.fit(X_train_scaled, y_train)
    train_acc = m.score(X_train_scaled, y_train)
    test_acc = m.score(X_test_scaled, y_test)
    print(f"K={k:2d} | Train: {train_acc:.3f} | Test: {test_acc:.3f}")