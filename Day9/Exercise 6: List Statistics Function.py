def list_stats(numbers):
    if not numbers:
        return {"count": 0, "total": 0, "average": 0, "minimum": None, "maximum": None}
        
    count = 0
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        count += 1
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
            
    average = total / count
    
    return {
        "count": count,
        "total": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum
    }

# Test execution
print(list_stats([1, 2, 3, 4, 5]))
