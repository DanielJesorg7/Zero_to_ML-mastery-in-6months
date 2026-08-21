from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


X, y = make_classification(n_samples=200, n_features=4, n_classes=2, 
                           n_informative=3, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Default tree (no depth limit)
model_1 = DecisionTreeClassifier( max_depth=2 ,random_state=42)
model_1.fit(X_train, y_train)
predictions = model_1.predict(X_test)

model_2 = DecisionTreeClassifier( max_depth=5 ,random_state=42)
model_2.fit(X_train, y_train)
predictions = model_2.predict(X_test)

model_3 = DecisionTreeClassifier( max_depth=None, random_state=42)
model_3.fit(X_train, y_train)
predictions = model_3.predict(X_test)

print("max_depth=2  | Train:", model_1.score(X_train, y_train), "| Test:", model_1.score(X_test, y_test))
print("max_depth=5  | Train:", model_2.score(X_train, y_train), "| Test:", model_2.score(X_test, y_test))
print("max_depth=None | Train:", model_3.score(X_train, y_train), "| Test:", model_3.score(X_test, y_test))

importance = pd.DataFrame({
    "feature": ["feat1", "feat2", "feat3", "feat4"],
    "importance": model_2.feature_importances_
}).sort_values("importance", ascending=False)

print(importance)