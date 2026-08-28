import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)
n5 = 400

data5 = {
    "tenure": np.random.randint(1, 61, n5),
    "monthly_charges": np.random.randint(1000, 20001, n5),
    "support_calls": np.random.randint(0, 11, n5),
    "contract_type": np.random.choice([1, 12, 24], n5)
}
df5 = pd.DataFrame(data5)
df5["churn"] = np.where(
    (df5["monthly_charges"] > 12000) & (df5["tenure"] < 12) &
    (df5["support_calls"] > 5) & (df5["contract_type"] == 1),
    1, 0
)

df5_encoded = pd.get_dummies(df5, columns=["contract_type"])
contract_cols5 = [c for c in df5_encoded.columns if "contract_type" in c]
df5_encoded[contract_cols5] = df5_encoded[contract_cols5].astype(int)

X5 = df5_encoded.drop("churn", axis=1)
y5 = df5_encoded["churn"]
X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5, test_size=0.2, random_state=42)

pipeline5 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('model', RandomForestClassifier(random_state=42))
])

param_grid5 = {
    'pca__n_components': [2, 3, 4],
    'model__n_estimators': [100, 200],
    'model__max_depth': [5, 10, None]
}

skf5 = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid5 = GridSearchCV(pipeline5, param_grid5, cv=skf5, scoring='accuracy')
grid5.fit(X5_train, y5_train)

print("Best params:", grid5.best_params_)
print("Best CV score:", grid5.best_score_)
print("Test accuracy:", grid5.best_estimator_.score(X5_test, y5_test))
print("PCA explained variance:", grid5.best_estimator_.named_steps['pca'].explained_variance_ratio_)

new_customer5 = pd.DataFrame({
    "tenure": [6], "monthly_charges": [15000], "support_calls": [7],
    "contract_type_1": [1], "contract_type_12": [0], "contract_type_24": [0]
})
new_customer5 = new_customer5[X5.columns]
proba5 = grid5.best_estimator_.predict_proba(new_customer5)
print("Churn probability [stay, churn]:", proba5)