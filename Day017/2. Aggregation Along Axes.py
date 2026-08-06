import numpy as np

# Create a 4x5 random integer array (from 1 to 100 inclusive)
arr = np.random.randint(1, 101, size=(4, 5))
print("Original 4x5 Array:\n", arr)

# 1. Sum of each row (axis=1 collapses columns to sum across the row)
print("\nSum of each row:", np.sum(arr, axis=1))

# 2. Mean of each column (axis=0 collapses rows to average down the column)
print("Mean of each column:", np.mean(arr, axis=0))

# 3. Max value in the entire array AND its flat position
max_val = np.max(arr)
max_flat_idx = np.argmax(arr)
# Unravel the flat index into 2D coordinates (row, column)
max_position = np.unravel_index(max_flat_idx, arr.shape)
print(f"Max value: {max_val}, Position: {max_position}")

# 4. Standard deviation of each column
print("Standard deviation of each column:", np.std(arr, axis=0))
