import numpy as np
import pandas as pd

np.random.seed(42)
n = 200

feature_1 = np.random.rand(n)
feature_2 = np.random.rand(n)
feature_3 = np.random.rand(n)
feature_4 = np.random.rand(n)
feature_5 = np.random.rand(n)

noise = np.random.rand(n) * 0.5
y = feature_1 * 2 + noise

df = pd.DataFrame({
   "feature_1": feature_1,
   "feature_2": feature_2,
   "feature_3": feature_3,
   "feature_4": feature_4,
   "feature_5": feature_5,
   "y": y
})

corr_matrix = df.corr()
print(corr_matrix["y"])

# Find highest and lowest absolute correlation (excluding y itself)
corr_with_y = corr_matrix["y"].drop("y").abs().sort_values(ascending=False)
print("Highest correlation:", corr_with_y.index[0], "=", corr_with_y.iloc[0])
print("Lowest correlation:", corr_with_y.index[-1], "=", corr_with_y.iloc[-1])

# Drop the feature with correlation CLOSEST TO 0
useless_feature = corr_with_y.index[-1]
df_reduced = df.drop(columns=[useless_feature])
print("Dropped:", useless_feature)
print("Original shape:", df.shape)
print("Reduced shape:", df_reduced.shape)
