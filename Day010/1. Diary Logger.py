from datetime import datetime

# Get user input
entry = input("Write your diary entry: ")

# Get current timestamp formatted as [YYYY-MM-DD HH:MM]
timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")

# Open file in append mode ('a') to prevent overwriting
with open("diary.txt", "a") as file:
    file.write(f"{timestamp}\n{entry}\n---\n")

print("Diary entry saved successfully.")
