import numpy as np

# Create two 3x3 matrices with values 1-9 and 10-18
mat1 = np.arange(1, 10).reshape(3, 3)
mat2 = np.arange(10, 19).reshape(3, 3)

print("Matrix 1:\n", mat1)
print("Matrix 2:\n", mat2)

# 1. Element-wise multiplication (*)
print("\nElement-wise multiplication:\n", mat1 * mat2)

# 2. Dot product (@ or np.dot)
print("\nDot product:\n", mat1 @ mat2)

# 3. Transpose of the first matrix
print("\nTranspose of the first matrix:\n", mat1.T)

# 4. Trace of the result (sum of diagonal elements of the dot product)
dot_result = mat1 @ mat2
print("\nTrace of the dot product result:", np.trace(dot_result))
