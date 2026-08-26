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

scores = cross_val_score(model, X, y, cv=5)
print("CV scores:", scores)
print("Mean:", scores.mean(), "Std:", scores.std())