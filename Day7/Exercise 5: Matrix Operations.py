# Create a 3x3 matrix using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# 1. Print the entire matrix (formatted nicely)
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

# 2. Print the main diagonal
main_diagonal = [matrix[i][i] for i in range(3)]
print(f"\nThe main diagonal: {main_diagonal}")

# 3. Print the sum of all elements
total_sum = sum(sum(row) for row in matrix)
print(f"The sum of all elements: {total_sum}")

# 4. Print the sum of each row
print("The sum of each row:")
for i, row in enumerate(matrix):
    print(f"Row {i+1} sum: {sum(row)}")
