import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Adeleke", "Daniel", "Sarah", "John"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 4],
    "math": [85, 90, 60],
    "english": [78, 82, 55]
})

# Left join = keep ALL rows from the LEFT table (students)
# Missing scores get NaN
merged = pd.merge(students, scores, on="student_id", how="left")

print("Before fill:")
print(merged)

# Fill missing scores with 0
merged["math"] = merged["math"].fillna(0)
merged["english"] = merged["english"].fillna(0)

print("\nAfter fill:")
print(merged)
