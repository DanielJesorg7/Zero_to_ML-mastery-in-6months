import pandas as pd

# Table 1: Student info
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Adeleke", "Daniel", "Sarah", "John"],
    "age": [25, 22, 24, 23]
})

# Table 2: Scores (notice student_id 3 is missing, student_id 5 doesn't exist in students)
scores = pd.DataFrame({
    "student_id": [1, 2, 4, 5],
    "math": [85, 90, 60, 78],
    "english": [78, 82, 55, 88]
})

# Inner join = ONLY keep rows where student_id exists in BOTH tables
# Result: student_id 3 (no scores) and 5 (no student info) are dropped
merged = pd.merge(students, scores, on="student_id", how="inner")

print(merged)
