import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)
n = 500

data = {
    "monthly_charges": np.random.randint(1000, 20000, n),
    "tenure_months": np.random.randint(1, 72, n),
    "support_calls": np.random.randint(0, 10, n),
    "contract_length": np.random.choice([1, 12, 24], n),
    "total_payments": np.random.randint(5000, 500000, n)
}
df = pd.DataFrame(data)

df["churn"] = np.where(
    (df["monthly_charges"] > 12000) & (df["tenure_months"] < 12) &
    (df["support_calls"] > 5) & (df["contract_length"] == 1),
    1, 0
)

X = df.drop("churn", axis=1)
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest
rf = RandomForestClassifier(n_estimators=150, max_depth=6, random_state=42)
rf.fit(X_train, y_train)
rf_predictions = rf.predict(X_test)

print("=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, rf_predictions))
print(confusion_matrix(y_test, rf_predictions))
print(classification_report(y_test, rf_predictions))

# Feature importance
importance = pd.DataFrame({
    "feature": ["monthly_charges", "tenure_months", "support_calls", "contract_length", "total_payments"],
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=False)

print(importance)

# New customer churn probability
new_customer = [[15000, 6, 7, 1, 30000]]
proba = rf.predict_proba(new_customer)
print("Churn probability (0=stay, 1=churn):", proba)

# Bonus: Decision Tree comparison
dt = DecisionTreeClassifier(max_depth=6, random_state=42)
dt.fit(X_train, y_train)
dt_predictions = dt.predict(X_test)

print("=== Decision Tree (comparison) ===")
print("Accuracy:", accuracy_score(y_test, dt_predictions))