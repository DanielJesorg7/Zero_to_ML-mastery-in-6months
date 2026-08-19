import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 8, 9],
    "sleep_hours": [8, 7, 6, 7, 5, 8, 6, 7, 5, 7, 4, 5, 8, 7],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

X = df[["study_hours", "sleep_hours"]]
y = df["passed"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy_score,")

print(accuracy_score(y_test, predictions))