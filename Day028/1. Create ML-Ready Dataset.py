import pandas as pd

data = {
    "study_hours": [2, 5, 3, 8, 1, 9, 4, 7, 2, 6],
    "sleep_hours": [8, 7, 6, 7, 5, 8, 6, 7, 5, 7],
    "attendance": [70, 85, 60, 95, 50, 90, 75, 88, 55, 92],
    "passed": [0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df.drop("passed", axis=1)
y = df["passed"]

print("X shape:", X.shape)
print("y shape:", y.shape)
