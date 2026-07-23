path = input("Enter a file path: ").strip()

# Detect slash type
slash = "\\" if "\\" in path else "/"

# Split into directory and full filename
directory, _, full_name = path.rpartition(slash)

# Handle case where path ends with slash (no filename)
if not full_name:
    print("Error: Path ends with a slash, no filename found.")
else:
    # Split filename and extension
    name_only, dot, extension = full_name.rpartition(".")

    print(f"Directory: {directory}")
    print(f"Full filename: {full_name}")
    
    if dot:  # Has extension
        print(f"File name (no ext): {name_only}")
        print(f"Extension: {extension}")
    else:
        print(f"File name (no ext): {full_name}")
        print("Extension: (none)")
