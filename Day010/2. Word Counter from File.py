# First, let's create the dummy input.txt file as requested
with open("input.txt", "w") as file:
    file.write("Hello World!\nWelcome to Python file handling.\nThis is a test file.")

# Program to read and analyze the file
try:
    with open("input.txt", "r") as file:
        lines = file.readlines()
        
    line_count = len(lines)
    word_count = 0
    char_count = 0
    
    for line in lines:
        char_count += len(line)
        word_count += len(line.split())

    # Write statistics to stats.txt
    with open("stats.txt", "w") as file:
        file.write(f"Lines: {line_count}\n")
        file.write(f"Words: {word_count}\n")
        file.write(f"Characters: {char_count}\n")
        
    print("Stats written to stats.txt successfully.")

except FileNotFoundError:
    print("Error: input.txt file not found.")
