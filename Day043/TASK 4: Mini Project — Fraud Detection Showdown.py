import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.datasets import make_classification


np.random.seed(42)
n = 500

# Normal transactions
amount = np.random.randint(1000, 50001, n)
frequency = np.random.randint(1, 31, n)
time_since_last = np.random.uniform(0, 30, n)
merchant_risk = np.random.uniform(0, 1, n)

# Inject 25 frauds
fraud_idx = np.random.choice(n, 25, replace=False)
amount[fraud_idx] = np.random.randint(200000, 500001, 25)
frequency[fraud_idx] = np.random.randint(40, 61, 25)
time_since_last[fraud_idx] = np.random.uniform(0, 1, 25)
merchant_risk[fraud_idx] = np.random.uniform(0.8, 1.0, 25)

df = pd.DataFrame({
    "amount": amount,
    "frequency": frequency,
    "time_since_last": time_since_last,
    "merchant_risk_score": merchant_risk
})
df["known_fraud"] = 0
df.loc[fraud_idx, "known_fraud"] = 1

X = df.drop("known_fraud", axis=1)
y = df["known_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

from sklearn.model_selection import cross_val_score

model_RF = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model_GB_default = GradientBoostingClassifier(random_state=42)
model_GB_tuned = GradientBoostingClassifier(random_state=42, learning_rate=0.1, n_estimators=100, max_depth=2)
    
    

scores_rf = cross_val_score(model_RF, X_train, y_train, cv=skf, scoring='accuracy')
scores_gb_default = cross_val_score(model_GB_default, X_train, y_train, cv=skf, scoring='accuracy')
scores_gb_tuned = cross_val_score(model_GB_tuned, X_train, y_train, cv=skf, scoring='accuracy')

print("RF mean CV accuracy:", scores_rf.mean())
print("GB default mean CV accuracy:", scores_gb_default.mean())
print("GB tuned mean CV accuracy:", scores_gb_tuned.mean())

model_GB_tuned.fit(X_train, y_train)         

y_pred_final = model_GB_tuned.predict(X_test)  

from sklearn.metrics import confusion_matrix, classification_report

print("Test Accuracy:", model_GB_tuned.score(X_test, y_test))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_final))
print("Classification Report:")
print(classification_report(y_test, y_pred_final))

print("Feature importances:", model_GB_tuned.feature_importances_)