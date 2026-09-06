import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import roc_curve, auc

np.random.seed(42)
n = 400

# 
age = np.random.randint(20, 80, n)
blood_pressure = np.random.randint(90, 180, n)
cholesterol = np.random.uniform(150, 300, n)
bmi = np.random.uniform(18, 35, n)



df = pd.DataFrame({
    "age": age,
    "blood_pressure": blood_pressure,
    "cholesterol": cholesterol,
    "bmi": bmi
})
disease = ((age > 50) & (cholesterol > 240) & (blood_pressure > 140)).astype(int)
df["disease"] = disease

X = df.drop("disease", axis=1)
y = df["disease"]
print(df["disease"].value_counts())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)

model =GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))

fpr, tpr, _ = roc_curve(y_test, proba)
roc_auc = auc(fpr, tpr)
print(f"AUC: {roc_auc:.3f}")


from sklearn.metrics import f1_score, precision_score, recall_score

best_recall = 0
best_thresh_medical = None

for thresh in np.arange(0.1, 0.9, 0.05):
    preds = (proba >= thresh).astype(int)
    p = precision_score(y_test, preds)
    r = recall_score(y_test, preds)
    
    if p >= 0.70 and r > best_recall:
        best_recall = r
        best_thresh_medical = thresh

if best_thresh_medical is not None:
    preds_final = (proba >= best_thresh_medical).astype(int)
    print(f"Chosen threshold: {best_thresh_medical:.2f}")
    print(f"Precision: {precision_score(y_test, preds_final):.3f}")
    print(f"Recall: {recall_score(y_test, preds_final):.3f}")
    print(f"F1: {f1_score(y_test, preds_final):.3f}")
else:
    print("No threshold met precision >= 0.70, falling back...")
    # fallback: best precision at recall >= 0.80 goes here
    
    
    
"""
recall matters more than precision in disease detection because a false negative (telling a sick patient they're healthy) can cost a life, while a false positive (telling a healthy patient to get more tests) costs time/money/anxiety but not their life
"""