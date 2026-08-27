import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)
n = 400

data = {
    "tenure": np.random.randint(1, 61, n),
    "monthly_charges": np.random.randint(1000, 20001, n),
    "support_calls": np.random.randint(0, 11, n),
    "contract_type": np.random.choice([1, 12, 24], n)
}
df = pd.DataFrame(data)

df["churn"] = np.where(
    (df["monthly_charges"] > 12000) & (df["tenure"] < 12) &
    (df["support_calls"] > 5) & (df["contract_type"] == 1),
    1, 0
)

df_encoded = pd.get_dummies(df, columns=["contract_type"])
contract_cols = [c for c in df_encoded.columns if "contract_type" in c]
df_encoded[contract_cols] = df_encoded[contract_cols].astype(int)

X = df_encoded.drop("churn", axis=1)
y = df_encoded["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=skf,
    scoring='accuracy'
)

grid.fit(X_train_scaled, y_train)

print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)

best_model = grid.best_estimator_
predictions = best_model.predict(X_test_scaled)
print("Test accuracy:", accuracy_score(y_test, predictions))

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": best_model.feature_importances_
}).sort_values("importance", ascending=False)
print(importance)

new_customer = pd.DataFrame({
    "tenure": [6],
    "monthly_charges": [15000],
    "support_calls": [7],
    "contract_type_1": [1],
    "contract_type_12": [0],
    "contract_type_24": [0]
})
new_customer = new_customer[X.columns]  # match training column order
new_customer_scaled = scaler.transform(new_customer)
proba = best_model.predict_proba(new_customer_scaled)
print("Churn probability [stay, churn]:", proba)