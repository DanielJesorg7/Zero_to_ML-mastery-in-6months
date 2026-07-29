def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_grade_message(grade):
    messages = {
        "A": "Excellent work! Keep it up.",
        "B": "Great job! Highly well done.",
        "C": "Good effort! Room to grow.",
        "D": "Passed, but you need more practice.",
        "F": "Do not give up! Try harder next time."
    }
    return messages.get(grade, "Invalid grade")

# Main Program
if __name__ == "__main__":
    try:
        user_score = float(input("Enter your score: "))
        final_grade = get_grade(user_score)
        motivational_message = get_grade_message(final_grade)
        print(f"Grade: {final_grade} - {motivational_message}")
    except ValueError:
        print("Please enter a valid numeric score.")
