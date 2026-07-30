# Setup: Create test numbers.txt containing valid integers and bad data
with open("numbers.txt", "w") as file:
    file.write("5\nabc\n12\n\n8\n")

def process_numbers(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return

    # Clear previous error logs
    open("errors.log", "w").close()

    for index, line in enumerate(lines, start=1):
        clean_line = line.strip()
        
        # Skip completely empty lines
        if not clean_line:
            continue
            
        try:
            # Convert to int
            number = int(clean_line)
            # Square it
            squared = number ** 2
            # Print result
            print(f"Line {index}: {number} squared is {squared}")
            
        except ValueError:
            # Handle non-number items without crashing
            with open("errors.log", "a") as err_file:
                err_file.write(f"Line {index}: '{clean_line}' is not a valid number.\n")

# Run the function
process_numbers("numbers.txt")
