from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
X = iris.data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

print(kmeans.labels_[:10])         
print(kmeans.inertia_)          # total within-cluster sum of squares
print(kmeans.cluster_centers_)  # coordinates of each centroid
