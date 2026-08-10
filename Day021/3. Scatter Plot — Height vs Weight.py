import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate 10 random heights (150-190 cm) and weights (50-90 kg)
heights = np.random.uniform(150, 190, 10)
weights = np.random.uniform(50, 90, 10)

# Calculate BMI: weight / (height / 100)**2
bmi = weights / (heights / 100) ** 2

# Define color category based on BMI condition
colors = ['red' if b > 25 else 'green' for b in bmi]

# Plotting the scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(heights, weights, c=colors, s=100, edgecolors='black')

plt.title("Height vs Weight (Colored by BMI)")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()
