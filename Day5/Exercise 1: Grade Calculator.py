score_input = input("Enter a score (0-100): ")
score = int(score_input)

if score < 0 or score > 100:
    print("Invalid score")

elif score >= 90:
    print("Grade: A")
    print("Excellent work!")

elif score >= 80:
    print("Grade: B")
    print("Great job!")

elif score >= 70:
    print("Grade: C")
    print("Good effort.")

elif score >= 60:
    print("Grade: D")
    print("You passed, but study harder.")

else:
    print("Grade: F")
    print("Failed. Time to retake.")
