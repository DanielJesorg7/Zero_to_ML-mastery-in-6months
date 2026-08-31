import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

np.random.seed(42)
X_normal = np.random.randn(300, 2)
X_outliers = np.random.uniform(4, 6, size=(20, 2))
X = np.vstack([X_normal, X_outliers])

model = IsolationForest(contamination=0.06, random_state=42)
model.fit(X)
preds = model.predict(X)

normal = X[preds == 1]
anomalies = X[preds == -1]

plt.figure(figsize=(8, 6))
plt.scatter(normal[:, 0], normal[:, 1], c='blue', label='Normal', alpha=0.6)
plt.scatter(anomalies[:, 0], anomalies[:, 1], c='red', label='Anomaly', alpha=0.8)
plt.title("Isolation Forest Anomaly Detection")
plt.legend()
plt.savefig("anomalies.png")
print("Plot saved as anomalies.png")
