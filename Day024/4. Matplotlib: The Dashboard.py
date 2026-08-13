import matplotlib.pyplot as plt

# Create a single figure with 2 subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left Subplot: Bar Chart ---
categories = ["A", "B", "C", "D"]
values = [10, 25, 15, 30]
bars = ax1.bar(categories, values, color="skyblue", edgecolor="black")

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 0.5,
        str(yval),
        ha="center",
        va="bottom",
    )

ax1.set_title("Category Values")
ax1.set_xlabel("Categories")
ax1.set_ylabel("Values")

# --- Right Subplot: Scatter Plot ---
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 4]
colors = ["red" if val > 3 else "blue" for val in y]

ax2.scatter(x, y, c=colors, s=100, edgecolor="black")
ax2.set_title("Conditional Point Colors")
ax2.set_xlabel("X Values")
ax2.set_ylabel("Y Values")

# Adjust layout and save image
plt.tight_layout()
plt.savefig("revision_chart.png", dpi=300)
plt.show()
print("Dashboard saved successfully as 'revision_chart.png'.")
