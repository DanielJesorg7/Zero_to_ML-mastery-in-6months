import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

np.random.seed(42)
n = 200

feature_1 = np.random.rand(n)
feature_2 = feature_1 + np.random.rand(n) * 0.05   # near-duplicate of feature_1
feature_3 = np.random.rand(n)
feature_4 = np.random.rand(n)

noise = np.random.rand(n) * 0.5
y = feature_1 + noise

df = pd.DataFrame({
    "feature_1": feature_1,
    "feature_2": feature_2,
    "feature_3": feature_3,
    "feature_4": feature_4,
    "y": y
})

X = df.drop("y", axis=1)
y = df["y"]

y_binary = (df["y"] > df["y"].median()).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Scale first
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# PCA on scaled train data
pca = PCA(n_components=2)
pca.fit(X_train_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total info kept:", sum(pca.explained_variance_ratio_))

X_train_pca = pca.transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Logistic Regression on PCA components
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train_pca, y_train)
predictions = model.predict(X_test_pca)
print("Accuracy:", accuracy_score(y_test, predictions))