import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(1)
data = {
    "sqft": np.random.randint(800, 5000, 100),
    "bedrooms": np.random.randint(1, 6, 100),
    "bathrooms": np.random.randint(1, 4, 100),
    "age": np.random.randint(0, 50, 100)
}
# Price formula (roughly realistic)
data["price"] = (data["sqft"] * 150 + 
                 data["bedrooms"] * 50000 + 
                 data["bathrooms"] * 30000 - 
                 data["age"] * 2000 + 
                 np.random.randint(-50000, 50000, 100))


df = pd.DataFrame(data)
print(df.isnull().sum())

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)  
r2 = r2_score(y_test, predictions)

print("MAE - " ,mae)
print("r2 - ", r2)

new_house = [[2500, 3, 2, 10]]
prediction = model.predict(new_house)
print(prediction)

