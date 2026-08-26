import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=300, n_features=5, n_redundant=0, random_state=1)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=skf)
    print(f"{name}")
    print("  Fold scores:", scores)
    print("  Mean:", scores.mean(), "Std:", scores.std())