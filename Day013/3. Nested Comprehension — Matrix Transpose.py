matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# One nested comprehension to switch rows and columns
transpose = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

print("Output:", transpose)
