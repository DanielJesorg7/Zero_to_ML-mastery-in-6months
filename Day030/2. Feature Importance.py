import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
model = LinearRegression()
from sklearn.metrics import mean_absolute_error, r2_score
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8],
    "sleep_hours": [8, 7, 6, 7, 5, 8, 6, 7, 5, 7, 6, 7, 8, 6],
    "attendance": [60, 70, 80, 85, 50, 90, 75, 88, 55, 92, 78, 82, 91, 85],
    "exam_score": [40, 45, 55, 60, 35, 75, 65, 80, 40, 88, 60, 70, 85, 78]
}

df = pd.DataFrame(data)

X = df[["study_hours", "sleep_hours", "attendance"]]
y = df["exam_score"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions) 
print("Actual:", y_test.values)

mae = mean_absolute_error(y_test, predictions)  
r2 = r2_score(y_test, predictions)

print("MAE - " ,mae)
print("r2 - ", r2)

print("model.coef" ,model.coef_)  
print("model.intercept",model.intercept_) 
