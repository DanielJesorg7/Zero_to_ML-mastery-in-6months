import numpy as np
import pandas as pd

data = {
    "name": ["Adeleke", "Daniel", "Sarah", "John", "Mary"],
    "gender": ["Male", "Male", "Female", "Male", "Female"],
    "city": ["Lagos", "Abuja", "Lagos", "Kano", "Abuja"]
}

df = pd.DataFrame(data)

df["gender_encoded"] = df["gender"].map({"Male": 0, "Female": 1})
df["city_encoded"] = df["city"].map({"Lagos": 0, "Abuja": 1, "Kano" : 2})

print(df["gender_encoded"])
print(df["city_encoded"])
