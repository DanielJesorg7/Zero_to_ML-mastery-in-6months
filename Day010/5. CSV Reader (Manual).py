# Setup: Create students.csv file
csv_data = """name,score
Adeleke,85
Daniel,92
Sarah,78"""

with open("students.csv", "w") as file:
    file.write(csv_data)

# Main program with manual CSV parsing and exception handling
try:
    with open("students.csv", "r") as file:
        lines = file.readlines()

    # Skip header and extract data
    students = []
    total_score = 0

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        name, score_str = line.split(",")
        score = int(score_str)
        students.append((name, score))
        total_score += score

    # Calculate average
    average_score = total_score / len(students)
    print(f"Average Score: {average_score:.2f}\n")

    # Print students scoring above average
    print("Students above average:")
    for name, score in students:
        if score > average_score:
            print(f"- {name}: {score}")

except FileNotFoundError:
    print("Error: students.csv file could not be found.")
