import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

# 90% Class 0, 10% Class 1
X = np.random.rand(100, 2)
y = np.array([0]*90 + [1]*10)

# Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dummy model: ALWAYS predicts the most frequent class (0)
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
preds = dummy.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print("But the model never predicted Class 1. Is it useful?")

print("The actual reason: it never predicts class 1 at all")