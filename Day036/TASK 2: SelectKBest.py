import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 200

feature_1 = np.random.rand(n)
feature_2 = np.random.rand(n)
feature_3 = np.random.rand(n)
feature_4 = np.random.rand(n)
feature_5 = np.random.rand(n)

noise = np.random.rand(n) * 0.5
y = feature_1 * 2 + noise

df = pd.DataFrame({
    "feature_1": feature_1,
    "feature_2": feature_2,
    "feature_3": feature_3,
    "feature_4": feature_4,
    "feature_5": feature_5,
    "y": y
})
X = df.drop("y", axis=1)
y = df["y"]

y_binary = (df["y"] > df["y"].median()).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# Fit on TRAIN only
selector = SelectKBest(score_func=f_classif, k=3)
selector.fit(X_train, y_train)

# See scores for ALL features
print(selector.scores_)

# Transform both train and test
X_train_selected = selector.transform(X_train)
X_test_selected = selector.transform(X_test)

# Which features were selected
selected_mask = selector.get_support()
selected_features = X.columns[selected_mask]
print("Selected features:", list(selected_features))

# Train Logistic Regression on selected features
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train_selected, y_train)
predictions = model.predict(X_test_selected)
print("Accuracy:", accuracy_score(y_test, predictions))
