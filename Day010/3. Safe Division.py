def safe_divide(a, b):
    try:
        # Check if inputs are numbers
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Invalid input"
        
        result = a / b
        
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
    else:
        return result

# Test cases
print(safe_divide(10, 2))       # Expected: 5.0
print(safe_divide(10, 0))       # Expected: Cannot divide by zero
print(safe_divide("10", 2))     # Expected: Invalid input
