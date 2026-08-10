import numpy as np
import matplotlib.pyplot as plt

# Mock data generation
days = [f"Day {i}" for i in range(1, 8)]
temp = [22, 24, 19, 23, 25, 28, 26]
rainfall = [5, 0, 12, 3, 0, 0, 8]
humidity = [60, 65, 80, 70, 55, 50, 62]
wind_speed = np.random.normal(12, 3, 100)

# Create a 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: Line plot of temperature over 7 days
axes[0, 0].plot(days, temp, marker='o', color='orange')
axes[0, 0].set_title("Temperature over 7 Days")
axes[0, 0].set_ylabel("Temp (°C)")

# Top-right: Bar chart of rainfall over 7 days
axes[0, 1].bar(days, rainfall, color='blue')
axes[0, 1].set_title("Rainfall over 7 Days")
axes[0, 1].set_ylabel("Rainfall (mm)")

# Bottom-left: Scatter of humidity vs temperature
axes[1, 0].scatter(temp, humidity, color='green')
axes[1, 0].set_title("Humidity vs Temperature")
axes[1, 0].set_xlabel("Temperature (°C)")
axes[1, 0].set_ylabel("Humidity (%)")

# Bottom-right: Histogram of wind speed
axes[1, 1].hist(wind_speed, bins=10, color='gray', edgecolor='black')
axes[1, 1].set_title("Histogram of Wind Speed")
axes[1, 1].set_xlabel("Speed (km/h)")

plt.tight_layout()
plt.show()
