import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression

X, y = make_classification(
    n_samples=200,       # Total number of samples
    n_features=20,       # Default number of features
    n_redundant=0,       # No redundant features as requested
    weights=[0.9, 0.1],  # 90% Class 0, 10% Class 1
    random_state=1       # Ensures exact 180/20 class split breakdown
)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Single split accuracy:", accuracy)


from sklearn.model_selection import KFold, StratifiedKFold

kf = KFold(n_splits=5)
kfold_scores = cross_val_score(model, X, y, cv=kf)
print("Regular KFold scores:", kfold_scores)
print("KFold mean:", kfold_scores.mean(), "std:", kfold_scores.std())

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
strat_scores = cross_val_score(model, X, y, cv=skf)
print("StratifiedKFold scores:", strat_scores)
print("StratifiedKFold mean:", strat_scores.mean(), "std:", strat_scores.std())