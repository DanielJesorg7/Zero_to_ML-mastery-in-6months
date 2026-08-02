names = ["Adeleke", "Daniel"]
scores = [85, 92]
grades = ["A", "A"]

# Convert scores to percentages (out of 100) using map
percentages = list(map(lambda x: f"{x}%", scores))

# Zip to print formatted rows
for name, score, grade in zip(names, percentages, grades):
    print(f"Name: {name} | Score: {score} | Grade: {grade}")
