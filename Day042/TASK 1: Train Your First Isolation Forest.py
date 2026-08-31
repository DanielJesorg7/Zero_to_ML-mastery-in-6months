import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

np.random.seed(42)
n = 300

# Normal data
X_normal = np.random.randn(n, 2)

# Inject 20 outliers
X_outliers = np.random.uniform(4, 6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

model = IsolationForest(contamination=0.06, random_state=42)
model.fit(X)

preds = model.predict(X)
scores = model.decision_function(X)

n_anomalies = (preds == -1).sum()
print(f"Found {n_anomalies} anomalies out of {len(X)}")

df = pd.DataFrame(X, columns=["f1", "f2"])
df["score"] = scores
df["pred"] = preds
print("5 most suspicious:")
print(df.nsmallest(5, "score"))
