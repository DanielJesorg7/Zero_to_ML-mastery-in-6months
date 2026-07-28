# 1. Numbers 1-10 as keys, cubes as values
drill_1 = {x: x**3 for x in range(1, 11)}

# 2. Dictionary from list where key=fruit, value=length
fruits = ["apple", "banana", "cherry"]
drill_2 = {fruit: len(fruit) for fruit in fruits}

# 3. Dictionary of even numbers 1-20 as keys, halves as values
drill_3 = {x: x / 2 for x in range(1, 21) if x % 2 == 0}

# 4. Invert a given dictionary
given_dict = {"a": 1, "b": 2, "c": 3}
drill_4 = {value: key for key, value in given_dict.items()}

# Print all four
print("Drill 1:", drill_1)
print("Drill 2:", drill_2)
print("Drill 3:", drill_3)
print("Drill 4:", drill_4)
