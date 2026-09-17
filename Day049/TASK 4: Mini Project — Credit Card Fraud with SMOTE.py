import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE


np.random.seed(42)
n = 1000

# ---------- Normal transactions ----------
amount = np.random.randint(1000, 50001, n)
frequency = np.random.randint(1, 31, n)
time_since_last = np.random.uniform(0, 30, n)
merchant_risk = np.random.uniform(0, 1, n)

# ---------- Inject 50 frauds ----------
fraud_idx = np.random.choice(n, 50, replace=False)

amount[fraud_idx] = np.random.randint(200000, 500001, 50)
frequency[fraud_idx] = np.random.randint(40, 61, 50)
time_since_last[fraud_idx] = np.random.uniform(0, 1, 50)
merchant_risk[fraud_idx] = np.random.uniform(0.8, 1.0, 50)

# ---------- Create DataFrame ----------
df = pd.DataFrame({
    "amount": amount,
    "frequency": frequency,
    "time_since_last": time_since_last,
    "merchant_risk_score": merchant_risk
})

df["known_fraud"] = 0
df.loc[fraud_idx, "known_fraud"] = 1


from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, accuracy_score

X = df.drop("known_fraud", axis=1)
y = df["known_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

from sklearn.metrics import confusion_matrix, classification_report

# Step 2 - No balancing
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred_1 = model.predict(X_test)
recall_1 = recall_score(y_test, y_pred_1, pos_label=1)

# Step 3 - class_weight balanced
model_2 = RandomForestClassifier(class_weight='balanced', random_state=42)
model_2.fit(X_train, y_train)
y_pred_2 = model_2.predict(X_test)
recall_2 = recall_score(y_test, y_pred_2, pos_label=1)

# Step 4 - SMOTE
smote = SMOTE(random_state=42)
X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)
model_3 = RandomForestClassifier(random_state=42)
model_3.fit(X_train_bal, y_train_bal)
y_pred_3 = model_3.predict(X_test)
recall_3 = recall_score(y_test, y_pred_3, pos_label=1)

# Comparison table
print("Method\t\tAccuracy\tRecall")
print(f"No balancing\t{accuracy_score(y_test, y_pred_1):.3f}\t\t{recall_1}")
print(f"class_weight\t{accuracy_score(y_test, y_pred_2):.3f}\t\t{recall_2}")
print(f"SMOTE\t\t{accuracy_score(y_test, y_pred_3):.3f}\t\t{recall_3}")

# Full breakdown for each
for name, y_pred in [("No balancing", y_pred_1), ("class_weight", y_pred_2), ("SMOTE", y_pred_3)]:
    print(f"\n--- {name} ---")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

# Which approach would you deploy for a real bank, and why?
# No balancing — it already achieves perfect recall (1.0) at zero extra
# complexity, cost, or synthetic-data risk. SMOTE and class_weight only
# earn their added complexity when there's an actual recall gap to close,
# which this dataset (cleanly separable fraud) doesn't have.