import numpy as np
import matplotlib.pyplot as plt

# Generate 200 normal exam scores
mean_val = 70
std_val = 15
scores = np.random.normal(mean_val, std_val, 200)

# Plotting the histogram with 15 bins
plt.figure(figsize=(6, 4))
plt.hist(scores, bins=15, color='purple', edgecolor='black', alpha=0.7)

# Add vertical line at the mean
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean ({mean_val})')

plt.title("Exam Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()
plt.show()
