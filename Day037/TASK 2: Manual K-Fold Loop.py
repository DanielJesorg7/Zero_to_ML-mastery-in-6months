import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=200, n_features=4, n_classes=2,
                           n_informative=3, n_redundant=0, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Single split accuracy:", accuracy)

from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
fold_scores = []

for train_idx, test_idx in kf.split(X):
    X_train_fold, X_test_fold = X[train_idx], X[test_idx]
    y_train_fold, y_test_fold = y[train_idx], y[test_idx]
    
    fold_model = LogisticRegression()
    fold_model.fit(X_train_fold, y_train_fold)
    score = fold_model.score(X_test_fold, y_test_fold)
    fold_scores.append(score)
    print("Fold score:", score)

print("Manual mean:", np.mean(fold_scores))
print("Manual std:", np.std(fold_scores))
scores = cross_val_score(model, X, y, cv=5)
print("CV scores:", scores)
print("Mean:", scores.mean(), "Std:", scores.std())