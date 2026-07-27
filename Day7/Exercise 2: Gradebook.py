gradebook = []

# Collect input for 5 students
for i in range(5):
    name = input(f"Enter student {i+1} name: ").strip()
    score = float(input(f"Enter {name}'s score: "))
    gradebook.append([name, score])

# 1. Print all students and scores
print("\n--- All Students and Scores ---")
for name, score in gradebook:
    print(f"{name}: {score}")

# 2. Find the highest score and who got it
highest_student, highest_score = gradebook[0]
for name, score in gradebook:
    if score > highest_score:
        highest_score = score
        highest_student = name
print(f"\nHighest score: {highest_score} by {highest_student}")

# 3. Calculate the average score
total_score = sum(score for name, score in gradebook)
average_score = total_score / len(gradebook)
print(f"Average score: {average_score:.2f}")

# 4. Find all students who scored above average
print("\nStudents scoring above average:")
for name, score in gradebook:
    if score > average_score:
        print(f"- {name} ({score})")
