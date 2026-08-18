import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)
data = {
    "years_exp": np.random.randint(0, 15, 50),
    "salary": np.random.randint(200000, 1000000, 50)
}
# Make salary roughly correlate with experience
data["salary"] = data["salary"] + data["years_exp"] * 50000

df = pd.DataFrame(data)
print(df.isnull().sum())

X = df[["years_exp"]]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)  
r2 = r2_score(y_test, predictions)

print("MAE - " ,mae)
print("r2 - ", r2)



plt.scatter(y_test,predictions)
plt.xlabel("actual salary")
plt.ylabel("predicted salary")
plt.show()