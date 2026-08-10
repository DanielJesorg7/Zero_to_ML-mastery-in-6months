import matplotlib.pyplot as plt

# Create data arrays
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [120, 150, 130, 170, 160]

# Plotting the line chart
plt.figure(figsize=(6, 4))
plt.plot(months, revenue, marker='o', color='b', linestyle='-')

# Customizing elements
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.grid(True)

# Save and display
plt.savefig("revenue.png")
plt.show()
