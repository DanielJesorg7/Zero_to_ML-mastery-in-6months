import matplotlib.pyplot as plt

# Create data arrays
students = ["Adeleke", "Daniel", "Sarah"]
math_scores = [85, 90, 72]
colors = ['skyblue', 'salmon', 'lightgreen']

# Plotting the bar chart
plt.figure(figsize=(6, 4))
bars = plt.bar(students, math_scores, color=colors)

# Customizing elements
plt.title("Student Math Scores")
plt.xlabel("Students")
plt.ylabel("Scores")

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, str(yval), ha='center', va='bottom')

plt.show()
