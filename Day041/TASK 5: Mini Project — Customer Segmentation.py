import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300

data = {
    "age": np.random.randint(18, 71, n),
    "income": np.random.randint(100000, 2000001, n),
    "purchase_freq": np.random.randint(0, 51, n),
    "support_tickets": np.random.randint(0, 11, n),
}
df = pd.DataFrame(data)   # <-- this line was missing

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

print(np.bincount(kmeans.labels_))

df["cluster"] = kmeans.labels_
print(df.groupby("cluster").mean())

# Cluster interpretation:
# Cluster 0: older (57), high income, HIGH purchase frequency (36), moderate tickets
#            -> loyal high-value customers
# Cluster 1: youngest (28), lower income, high purchase frequency (31), moderate tickets
#            -> young engaged spenders, price-sensitive but active
# Cluster 2: middle-aged (46), high income similar to cluster 0, but LOW purchase
#            frequency (9) -> disengaged/inactive high-income customers,
#            worth targeting for re-engagement despite having money to spend

new_customer = pd.DataFrame({
    "age": [28],
    "income": [250000],
    "purchase_freq": [8],
    "support_tickets": [7]
})

new_customer_scaled = scaler.transform(new_customer)
predicted_cluster = kmeans.predict(new_customer_scaled)
print("New customer belongs to cluster:", predicted_cluster)