import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
np.random.seed(42)
n = 200

# Features: age, blood_pressure, cholesterol
data = {
    "age": np.random.randint(20, 80, n),
    "blood_pressure": np.random.randint(90, 180, n),
    "cholesterol": np.random.randint(150, 300, n)
}
df = pd.DataFrame(data)

# Target: 1 = Disease, 0 = Healthy (imbalanced: 30% disease)
df["disease"] = np.where(
    (df["age"] > 50) & (df["cholesterol"] > 240), 
    1, 
    np.random.choice([0, 1], n, p=[0.85, 0.15])
)

X = df.drop("disease", axis=1)
y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

cm = confusion_matrix(y_test, predictions)
print(cm)

tn, fp, fn, tp = cm.ravel()

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

print(classification_report(y_test, predictions, target_names=["Healthy", "Disease"]))

# Optimize for RECALL — a false negative here means telling a sick
# patient they're healthy, which could delay life-saving treatment.
# A false positive just means extra testing/inconvenience.
# Current recall (0.62) is too low for real hospital deployment —
# 5 out of 13 actual disease cases were missed.