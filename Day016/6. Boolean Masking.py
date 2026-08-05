import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65, 70, 85])

# Get all values > 40
print("Values > 40:", arr[arr > 40])

# Get all values divisible by 10
print("Values divisible by 10:", arr[arr % 10 == 0])

# Count how many values are > 50
print("Count of values > 50:", np.sum(arr > 50))

# Replace all values < 30 with 0 (in-place)
arr[arr < 30] = 0
print("Array after replacing values < 30 with 0:\n", arr)
