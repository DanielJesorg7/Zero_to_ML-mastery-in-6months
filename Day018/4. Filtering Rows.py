import pandas as pd

# Create a DataFrame of 5 students
student_data = {
    "name": ["Adeleke", "Daniel", "Sarah", "John", "Mary"],
    "math": [85, 90, 72, 60, 95],
    "english": [78, 82, 95, 55, 92],
    "physics": [90, 88, 85, 70, 98]
}
df_students = pd.DataFrame(student_data)

# Filter: Students with math > 80
math_above_80 = df_students[df_students["math"] > 80]
print("--- Math > 80 ---")
print(math_above_80)

# Filter: Students with average score > 85 (create avg column first)
df_students["avg"] = df_students[["math", "english", "physics"]].mean(axis=1)
avg_above_85 = df_students[df_students["avg"] > 85]
print("\n--- Average Score > 85 ---")
print(avg_above_85)

# Filter: Students who passed all subjects (all > 60)
passed_all = df_students[
    (df_students["math"] > 60) & 
    (df_students["english"] > 60) & 
    (df_students["physics"] > 60)
]
print("\n--- Passed All Subjects (> 60) ---")
print(passed_all)
