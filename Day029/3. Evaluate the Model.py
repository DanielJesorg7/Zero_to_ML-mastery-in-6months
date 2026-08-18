import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "exam_score": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
}
df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["exam_score"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)  
r2 = r2_score(y_test, predictions)

print("MAE - " ,mae)
print("r2 - ", r2)