import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X3, y3 = make_classification(n_samples=300, n_features=5, n_classes=2,
                             n_informative=3, n_redundant=0, random_state=1)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)

pipeline3 = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC(random_state=42))
])

param_grid3 = {
    'model__C': [0.1, 1, 10, 100],
    'model__kernel': ['linear', 'rbf'],
    'model__gamma': ['scale', 'auto']
}

grid3 = GridSearchCV(pipeline3, param_grid3, cv=5, scoring='accuracy')
grid3.fit(X3_train, y3_train)

print("Best params:", grid3.best_params_)
print("Best CV score:", grid3.best_score_)
print("Test accuracy:", grid3.best_estimator_.score(X3_test, y3_test))