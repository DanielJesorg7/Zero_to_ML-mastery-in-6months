students = {
    "Adeleke": {"math": 85, "english": 78, "science": 90},
    "Daniel": {"math": 90, "english": 82, "science": 88},
    "Sarah": {"math": 72, "english": 95, "science": 85}
}

# 1. Print each student's average score
student_averages = {}
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    student_averages[name] = avg
    print(f"{name}'s average score: {avg:.2f}")

# 2. Print the student with the highest average
highest_student = max(student_averages, key=student_averages.get)
print(f"Student with highest average: {highest_student} ({student_averages[highest_student]:.2f})")

# 3. Print the subject with the highest class average
subjects_list = ["math", "english", "science"]
subject_averages = {}
for sub in subjects_list:
    sub_avg = sum(students[name][sub] for name in students) / len(students)
    subject_averages[sub] = sub_avg

highest_subject = max(subject_averages, key=subject_averages.get)
print(f"Subject with highest class average: {highest_subject} ({subject_averages[highest_subject]:.2f})")
