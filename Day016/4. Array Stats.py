import numpy as np

# Create a random array
rand_arr = np.random.randint(1, 100, size=20)
print("Random Array:\n", rand_arr)

# Mean, median, std, min, max
print(f"Mean: {np.mean(rand_arr)}")
print(f"Median: {np.median(rand_arr)}")
print(f"Std Dev: {np.std(rand_arr)}")
print(f"Min: {np.min(rand_arr)}, Max: {np.max(rand_arr)}")

# Sum of all elements
print(f"Sum: {np.sum(rand_arr)}")

# Indices of values > 50 (using boolean indexing/where)
indices = np.where(rand_arr > 50)[0]
print(f"Indices of values > 50: {indices}")
