def convert_temp(value, from_unit, to_unit):
    valid_units = {"C", "F", "K"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return "Invalid unit"
        
    if from_unit == to_unit:
        return round(float(value), 2)
        
    # Convert input to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
        
    # Convert Celsius to target unit
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "K":
        result = celsius + 273.15
        
    return round(result, 2)

# Test cases
print(convert_temp(25, "C", "F"))    # Expected: 77.0
print(convert_temp(100, "F", "C"))   # Expected: 37.78
print(convert_temp(0, "C", "K"))     # Expected: 273.15
