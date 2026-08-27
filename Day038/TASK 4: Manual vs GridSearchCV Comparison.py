import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=200, n_features=4, n_classes=2,
                           n_informative=3, n_redundant=0, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

max_depths = [3, 5, 10]
n_estimators_list = [50, 100]

best_score = 0
best_params = None

for depth in max_depths:
    for n_est in n_estimators_list:
        model = RandomForestClassifier(max_depth=depth, n_estimators=n_est, random_state=42)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(f"max_depth={depth}, n_estimators={n_est} -> accuracy={score:.4f}")
        
        if score > best_score:
            best_score = score
            best_params = (depth, n_est)

print("Best combination:", best_params, "with accuracy:", best_score)


from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 10],
    'n_estimators': [50, 100]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid.fit(X_train, y_train)

print("GridSearchCV best params:", grid.best_params_)
print("GridSearchCV best CV score:", grid.best_score_)
print("Manual best params:", best_params)
print("Manual best test score:", best_score)

"""GridSearchCV's answer deserves more trust because it's cross-validated, not because it happens to agree or disagree on which specific params win — the reliability comes from the evaluation method, not the resulting number's size.
"""