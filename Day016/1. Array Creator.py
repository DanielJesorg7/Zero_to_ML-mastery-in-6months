import numpy as np

def create_arrays():
    # 1D array of numbers 10 to 50 (inclusive)
    arr1 = np.arange(10, 51)
    
    # 2D 4x4 array of zeros
    arr2 = np.zeros((4, 4))
    
    # 2D 3x3 array of ones with dtype float
    arr3 = np.ones((3, 3), dtype=float)
    
    # Array of 20 evenly spaced numbers between 0 and 1
    arr4 = np.linspace(0, 1, 20)
    
    return arr1, arr2, arr3, arr4

# Generate arrays
arrays = create_arrays()

# Print each with shape and dtype
for i, arr in enumerate(arrays, 1):
    print(f"Array {i}:")
    print(arr)
    print(f"Shape: {arr.shape}, Dtype: {arr.dtype}\n")
