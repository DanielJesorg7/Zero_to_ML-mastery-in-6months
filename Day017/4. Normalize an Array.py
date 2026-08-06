import numpy as np

# Create a random array of 50 floats (0 to 100)
random_floats = np.random.uniform(0, 100, size=50)

def normalize(arr):
    # Calculate global min and max values
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    
    # Apply min-max feature scaling formula
    return (arr - arr_min) / (arr_max - arr_min)

normalized_floats = normalize(random_floats)
print("First 5 normalized values:", normalized_floats[:5])
print("Normalized Min (should be 0.0):", np.min(normalized_floats))
print("Normalized Max (should be 1.0):", np.max(normalized_floats))
