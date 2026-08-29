import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)
n = 500

data = {
    "age": np.random.randint(18, 71, n),
    "income": np.random.randint(100000, 2000001, n),
    "purchase_freq": np.random.randint(0, 51, n),
    "support_tickets": np.random.randint(0, 11, n),
    "city": np.random.choice(['Lagos', 'Abuja', 'Kano', 'Port Harcourt'], n),
    "gender": np.random.choice(['Male', 'Female'], n)
}
df = pd.DataFrame(data)
df["churn"] = np.where(
    (df["support_tickets"] > 5) & (df["purchase_freq"] < 10) & (df["income"] < 500000),
    1, 0
)
df_encoded = pd.get_dummies(df, columns=["city", "gender"])
bool_cols = df_encoded.select_dtypes(include='bool').columns
df_encoded[bool_cols] = df_encoded[bool_cols].astype(int)

X = df_encoded.drop("churn", axis=1)
y = df_encoded["churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
winning_pipeline = Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier(random_state=42))])
param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [5, 10, None],
    'model__min_samples_split': [2, 5]
}
grid = GridSearchCV(winning_pipeline, param_grid, cv=skf, scoring='accuracy')
grid.fit(X_train, y_train)
best_model = grid.best_estimator_

new_customers = pd.DataFrame({
    "age": [25, 45, 33],
    "income": [300000, 1200000, 600000],
    "purchase_freq": [5, 30, 15],
    "support_tickets": [8, 1, 3],
    "city": ['Lagos', 'Abuja', 'Kano'],
    "gender": ['Male', 'Female', 'Male']
})

new_encoded = pd.get_dummies(new_customers, columns=["city", "gender"])
for col in X.columns:
    if col not in new_encoded.columns:
        new_encoded[col] = 0
new_encoded = new_encoded[X.columns]

predictions = best_model.predict(new_encoded)
probabilities = best_model.predict_proba(new_encoded)

for i, (pred, proba) in enumerate(zip(predictions, probabilities)):
    label = chr(65 + i)
    print(f"Customer {label}: prediction={pred}, churn probability={proba[1]:.4f}")

# SUMMARY:
# Winner of shootout: RandomForest (verify against your Task 2 output)
# Best hyperparameters: see grid.best_params_ from Task 3
# Best CV score: see grid.best_score_ from Task 3
# Most important feature: see Task 4's feature importance output