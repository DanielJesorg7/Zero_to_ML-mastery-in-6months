from collections import Counter

# First, create the app.log file as requested in the prompt
log_content = """ERROR: Database connection failed
INFO: Server started
ERROR: Timeout occurred
WARNING: Low memory
ERROR: Database connection failed"""

with open("app.log", "w") as f:
    f.write(log_content.strip())

# Read and analyze the log file
errors = 0
warnings = 0
infos = 0
error_messages = []

with open("app.log", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("ERROR:"):
            errors += 1
            error_messages.append(line.replace("ERROR:", "").strip())
        elif line.startswith("WARNING:"):
            warnings += 1
        elif line.startswith("INFO:"):
            infos += 1

# Find most common error message
counter = Counter(error_messages)
most_common_error = counter.most_common(1)[0][0] if error_messages else "None"

# Print results
print(f"Total Errors: {errors}, Warnings: {warnings}, Info: {infos}")
print(f"Most common error message: {most_common_error}")

# Write summary report
with open("log_report.txt", "w") as report:
    report.write(f"Log Analysis Summary\n")
    report.write(f"--------------------\n")
    report.write(f"Errors: {errors}\n")
    report.write(f"Warnings: {warnings}\n")
    report.write(f"Info: {infos}\n")
    report.write(f"Most Common Error: {most_common_error}\n")
