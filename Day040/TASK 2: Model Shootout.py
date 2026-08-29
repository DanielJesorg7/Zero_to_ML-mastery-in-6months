import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

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

pipelines = {
    "LogisticRegression": Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(random_state=42))]),
    "RandomForest": Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))]),
    "SVM": Pipeline([('scaler', StandardScaler()), ('model', SVC(kernel='rbf', random_state=42))])
}

results = {}
for name, pipe in pipelines.items():
    scores = cross_val_score(pipe, X_train, y_train, cv=skf)
    results[name] = scores.mean()
    print(f"{name}: mean={scores.mean():.4f}, std={scores.std():.4f}")

winner = max(results, key=results.get)
print("Winner:", winner)