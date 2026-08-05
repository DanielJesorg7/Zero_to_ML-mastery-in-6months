import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# The element at row 2, col 3 (0-indexed -> row index 2, col index 3)
print("Element at row 2, col 3:", matrix[2, 3])

# The first row
print("First row:", matrix[0])

# The last column
print("Last column:", matrix[:, -1])

# The 2x2 sub-matrix in the center
print("2x2 center sub-matrix:\n", matrix[1:3, 1:3])
