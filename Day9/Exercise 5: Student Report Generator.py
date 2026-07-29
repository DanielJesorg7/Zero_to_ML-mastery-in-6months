def generate_report(name, **subjects):
    print(f"STUDENT REPORT: {name}")
    print("-" * 30)
    
    if not subjects:
        print("No subject data available.")
        return

    total_score = 0
    for subject, score in subjects.items():
        print(f"{subject}: {score}")
        total_score += score
        
    avg_score = total_score / len(subjects)
    status = "Pass" if avg_score >= 60 else "Fail"
    
    print("-" * 30)
    print(f"Average: {round(avg_score, 1)}")
    print(f"Status: {status}")

# Test execution
generate_report("Adeleke", math=85, english=92, physics=78)
