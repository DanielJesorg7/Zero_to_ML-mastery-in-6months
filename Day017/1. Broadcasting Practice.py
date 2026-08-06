import numpy as np

# Create the initial data structures
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row = np.array([10, 20, 30])
col = np.array([[100], [200], [300]])

# Print operations and explain broadcasting behavior
print("matrix + row:\n", matrix + row)
# Explanation: 'row' has shape (3,). NumPy automatically expands it to shape (1, 3) 
# and then replicates it along axis 0 to match matrix's shape (3, 3). This broadcasts across rows.

print("\nmatrix + col:\n", matrix + col)
# Explanation: 'col' has shape (3, 1). NumPy replicates its values along axis 1 
# to match matrix's shape (3, 3). This broadcasts down columns.
