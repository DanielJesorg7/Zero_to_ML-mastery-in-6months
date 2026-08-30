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
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
for k, inertia in zip(range(1, 11), inertias):
    print(f"K={k}, inertia={inertia:.2f}")

'''
yes, the elbow is at K=3, and that matches the fact that Iris genuinely has 3 species
'''