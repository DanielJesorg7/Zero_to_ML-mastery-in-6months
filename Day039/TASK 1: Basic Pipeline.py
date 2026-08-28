import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=200, n_features=4, n_classes=2,
                           n_informative=3, n_redundant=0, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline version
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])
pipeline.fit(X_train, y_train)
pipeline_predictions = pipeline.predict(X_test)
print("Pipeline accuracy:", accuracy_score(y_test, pipeline_predictions))

# Manual version
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

manual_model = LogisticRegression(random_state=42)
manual_model.fit(X_train_scaled, y_train)
manual_predictions = manual_model.predict(X_test_scaled)
print("Manual accuracy:", accuracy_score(y_test, manual_predictions))