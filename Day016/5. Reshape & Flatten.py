import numpy as np

base_arr = np.arange(12)
print(f"Original: {base_arr.shape}")

# Reshape to 3x4
arr_3x4 = base_arr.reshape(3, 4)
print(f"Reshape to 3x4 shape: {arr_3x4.shape}")

# Reshape to 4x3
arr_4x3 = base_arr.reshape(4, 3)
print(f"Reshape to 4x3 shape: {arr_4x3.shape}")

# Reshape to 2x6
arr_2x6 = base_arr.reshape(2, 6)
print(f"Reshape to 2x6 shape: {arr_2x6.shape}")

# Flatten back to 1D
flattened = arr_2x6.flatten()
print(f"Flattened back to 1D shape: {flattened.shape}")
