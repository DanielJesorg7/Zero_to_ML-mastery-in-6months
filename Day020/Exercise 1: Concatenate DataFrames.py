import pandas as pd

# Two separate classes of students
class_a = pd.DataFrame({
    "name": ["Adeleke", "Daniel"],
    "math": [85, 90],
    "english": [78, 82]
})

class_b = pd.DataFrame({
    "name": ["Sarah", "John"],
    "math": [72, 60],
    "english": [95, 55]
})

print("Class A shape:", class_a.shape)
print("Class B shape:", class_b.shape)

# axis=0 means stack vertically (add rows)
combined = pd.concat([class_a, class_b], axis=0)

print("\nCombined shape:", combined.shape)
print(combined)

# axis=1 would stack side by side (add columns) — not useful here
# but this is how you do it:
# side_by_side = pd.concat([class_a, class_b], axis=1)
