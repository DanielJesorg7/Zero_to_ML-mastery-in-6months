
from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
X = iris.data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

print(kmeans.labels_)           # cluster number for each sample
print(kmeans.inertia_)          # total within-cluster sum of squares
print(kmeans.cluster_centers_)  # coordinates of each centroid

inertias = []
from sklearn.metrics import silhouette_score

silhouette_scores = []
for k in range(2, 9):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    labels = km.labels_
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)
    print(f"K={k}, silhouette={score:.4f}")

from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, kmeans.labels_)
print(score)
