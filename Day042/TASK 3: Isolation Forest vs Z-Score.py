import numpy as np
from sklearn.ensemble import IsolationForest

np.random.seed(42)
X_normal = np.random.randn(300, 2)
X_outliers = np.random.uniform(4, 6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

# Method A: Isolation Forest
iso = IsolationForest(contamination=0.06, random_state=42)
iso.fit(X)
iso_preds = iso.predict(X)
iso_anomalies = iso_preds == -1

# Method B: Z-Score
means = X.mean(axis=0)
stds = X.std(axis=0)
z_scores = np.abs((X - means) / stds)
z_anomalies = (z_scores > 3).any(axis=1)

both = (iso_anomalies & z_anomalies).sum()
only_iso = (iso_anomalies & ~z_anomalies).sum()
only_z = (~iso_anomalies & z_anomalies).sum()

print(f"Both methods: {both}")
print(f"Only Isolation Forest: {only_iso}")
print(f"Only Z-Score: {only_z}")
