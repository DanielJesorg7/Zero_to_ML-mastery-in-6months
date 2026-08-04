import json

def read_numbers(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                continue  # Skips invalid lines
    return numbers

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

def save_results(numbers, filename):
    with open(filename, 'w') as f:
        json.dump(numbers, f)

def main():
    # Setup a dummy input file for demonstration purposes
    with open("input.txt", "w") as f:
        f.write("1\n2\nthree\n4\n5\n6\n")

    # Pipeline sequence execution
    nums = read_numbers("input.txt")
    evens = filter_even(nums)
    squared = square_numbers(evens)
    save_results(squared, "output.json")
    
    print("Pipeline finished. Results saved to output.json")

if __name__ == "__main__":
    main()
