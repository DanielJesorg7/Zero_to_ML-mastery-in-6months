import numpy as np

# Create a 5x5 random integer matrix between 0 and 100
arr_bool = np.random.randint(0, 100, size=(5, 5))
print("Original Matrix:\n", arr_bool)

# 1. Count of values > 50
count_gt_50 = np.sum(arr_bool > 50)
print(f"\nCount of values > 50: {count_gt_50}")

# 2. Percentage of values > 50
percentage_gt_50 = np.mean(arr_bool > 50) * 100
print(f"Percentage of values > 50: {percentage_gt_50}%")

# 3. Sum of all even numbers
even_mask = (arr_bool % 2 == 0)
sum_evens = np.sum(arr_bool[even_mask])
print(f"Sum of all even numbers: {sum_evens}")

# 4. Replace all odd numbers with -1 (in-place modification)
arr_bool[arr_bool % 2 != 0] = -1
print("\nMatrix after replacing odd numbers with -1:\n", arr_bool)
