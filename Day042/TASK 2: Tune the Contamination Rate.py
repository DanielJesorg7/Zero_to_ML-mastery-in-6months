import numpy as np
from sklearn.ensemble import IsolationForest

np.random.seed(42)
X_normal = np.random.randn(300, 2)
X_outliers = np.random.uniform(4, 6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

for cont in [0.02, 0.06, 0.15]:
    model = IsolationForest(contamination=cont, random_state=42)
    model.fit(X)
    preds = model.predict(X)
    n_anomalies = (preds == -1).sum()
    print(f"contamination={cont:.2f} -> {n_anomalies} anomalies")
