import numpy as np

np.random.seed(42)
matrix = np.random.randint(low =10,high = 99,size = (5,5))
print(matrix)
row_sums = matrix.sum(axis=1)
print("sum.of each rows")
print(row_sums)
print("sum of each columns")
column_sums = matrix.sum(axis=0)
print(column_sums)

max_overall = matrix.max()
print("Max value")
print(max_overall)

positions = np.argwhere(matrix == max_overall)
print("max value positions")
print(positions)

maskk = matrix > 50
print("maskk")
print(maskk)

