import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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
predictions = best_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
cm = confusion_matrix(y_test, predictions)
print("Confusion matrix:\n", cm)
print(classification_report(y_test, predictions))

tn, fp, fn, tp = cm.ravel()
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)
print(f"Manual Precision: {precision:.4f}")
print(f"Manual Recall: {recall:.4f}")
print(f"Manual F1: {f1:.4f}")

importances = pd.DataFrame({
    "feature": X.columns,
    "importance": best_model.named_steps['model'].feature_importances_
}).sort_values("importance", ascending=False)
print("Feature importances:\n", importances)