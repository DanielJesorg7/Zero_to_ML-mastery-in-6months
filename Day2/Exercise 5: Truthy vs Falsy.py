
test_values = [
    0,
    1,
    "",
    "Hello",
    [],

    None
]

for val in test_values:
    
    print(f"Value: {repr(val):<12} -> Boolean: {bool(val)}")
