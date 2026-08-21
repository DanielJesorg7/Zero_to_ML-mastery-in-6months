import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)
n = 300

data = {
    "income": np.random.randint(200000, 2000000, n),
    "credit_score": np.random.randint(300, 850, n),
    "debt_ratio": np.random.uniform(0.1, 0.9, n),
    "employment_years": np.random.randint(0, 20, n)
}
df = pd.DataFrame(data)

df["approved"] = np.where(
    (df["income"] > 800000) & (df["credit_score"] > 600) & (df["debt_ratio"] < 0.5),
    1, 0
)

X = df.drop("approved", axis=1)
y = df["approved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("=== Decision Tree ===")
print("Accuracy:", accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# Feature importance
importance = pd.DataFrame({
    "feature": ["income", "credit_score", "debt_ratio", "employment_years"],
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

print(importance)

# New applicant prediction
new_applicant = [[1200000, 720, 0.3, 5]]
prediction = model.predict(new_applicant)
print("Prediction for new applicant (1=approved, 0=denied):", prediction)

# Bonus: Logistic Regression comparison
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_predictions = log_model.predict(X_test)

print("=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, log_predictions))