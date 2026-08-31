import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

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

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)
df["pred"] = model.predict(X)

# Evaluate
detected_frauds = ((df["pred"] == -1) & (df["known_fraud"] == 1)).sum()
false_positives = ((df["pred"] == -1) & (df["known_fraud"] == 0)).sum()
print(f"Known frauds caught: {detected_frauds}/25")
print(f"False positives: {false_positives}")

# Most suspicious
df["score"] = model.decision_function(X)
print("Top 5 suspicious:")
print(df.nsmallest(5, "score")[["amount", "frequency", "score"]])

# New transaction
new_txn = pd.DataFrame({
    "amount": [350000],
    "frequency": [45],
    "time_since_last": [0.5],
    "merchant_risk_score": [0.95]
})
pred = model.predict(new_txn)
print("Fraud prediction (-1=fraud):", pred[0])
