import numpy as np
import pandas as pd

np.random.seed(1)
data = {
    "name": [f"Emp_{i}" for i in range(1, 21)],
    "department": np.random.choice(["Engineering", "Sales", "HR"], 20),
    "years_experience": np.random.randint(0, 15, 20),
    "salary": np.random.randint(200000, 1000000, 20),
    "performance_rating": np.random.choice(["Poor", "Average", "Good", "Excellent"], 20)
}


df = pd.DataFrame(data)

df["department_encoded"] = df["department"].map({"Engineering": 0, "Sales": 1, "HR" : 2})

df["performance_rating_encoded"] = df["performance_rating"].map({"Poor": 0, "Average": 1, "Good" : 2, "Excellent" : 3})

print(df["department_encoded"])
print(df["performance_rating_encoded"])

def experience_category(row):
    if row["years_experience"] < 3:
        return "junior"
    elif 3 <= row["years_experience"] <= 7:
        return "mid"
    else:
        return "senior"

df["experience_category"] = df.apply(experience_category, axis=1)
print(df["experience_category"])

df["salary_scaled"] = (df["salary"] - df["salary"].min()) / (df["salary"].max() - df["salary"].min())

print(df["salary_scaled"])

clean_df = df.drop(columns=["salary"])
correlation_matrix = clean_df.corr(numeric_only=True)

print(correlation_matrix)
# idk years of experibce seem tocorrelate more