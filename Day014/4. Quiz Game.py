questions = [
    {
        "q": "What is 2+2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "q": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "q": "Which language is used for Android apps?",
        "options": ["A) Swift", "B) Kotlin", "C) C#", "D) Ruby"],
        "answer": "B"
    },
    {
        "q": "What is the boiling point of water?",
        "options": ["A) 50°C", "B) 80°C", "C) 100°C", "D) 120°C"],
        "answer": "C"
    },
    {
        "q": "How many continents are there?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    }
]

score = 0

for idx, q in enumerate(questions, 1):
    print(f"\nQuestion {idx}: {q['q']}")
    for option in q['options']:
        print(option)
    
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_ans == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {q['answer']}.")

percentage = (score / len(questions)) * 100
print(f"\n--- Final Results ---")
print(f"Score: {score}/{len(questions)}")
print(f"Percentage: {percentage}%")
