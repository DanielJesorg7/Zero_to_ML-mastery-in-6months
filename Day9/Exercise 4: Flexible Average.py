def average(*numbers):
    if not numbers:
        return 0
    
    total = 0
    for num in numbers:
        total += num
        
    return round(total / len(numbers), 2)

# Test cases
print(average(10, 20, 30))      # Expected: 20.0
print(average(5, 15))          # Expected: 10.0
print(average())               # Expected: 0
print(average(1, 2, 3, 4, 5))  # Expected: 3.0
