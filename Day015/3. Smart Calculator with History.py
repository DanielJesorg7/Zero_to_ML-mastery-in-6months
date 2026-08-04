import json
from datetime import datetime

def smart_calculate(a, b, op):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    elif op == "**":
        result = a ** b
    elif op == "%":
        result = a % b
    else:
        raise ValueError(f"Invalid operation: {op}")
    
    # Log to history
    entry = {
        "timestamp": datetime.now().isoformat(),
        "a": a,
        "b": b,
        "operation": op,
        "result": result
    }
    
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []
    
    history.append(entry)
    
    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)
    
    return result, len(history)

# Main program
if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /, **, %): ").strip()
        
        result, count = smart_calculate(a, b, op)
        print(f"Result: {result}")
        print(f"Total calculations so far: {count}")
        
    except ValueError as e:
        print(f"Error: {e}")
