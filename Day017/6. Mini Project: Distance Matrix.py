import numpy as np

# Initialize the 3 spatial coordinates
points = np.array([[0, 0],
                   [3, 4],
                   [6, 8]])

# Vectorized solution utilizing broadcasting mechanics
# Reshaping points to (3, 1, 2) and (1, 3, 2) lets NumPy calculate differences 
# between every pairing arrangement automatically across a grid matrix.
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]

# Calculate Euclidean distance: sqrt(dx^2 + dy^2) summed over the coordinate elements (axis=-1)
dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))

print("Pairwise Distance Matrix (3x3):\n", dist_matrix)
