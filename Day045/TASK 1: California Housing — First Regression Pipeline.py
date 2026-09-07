import joblib 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.pipeline import Pipeline



data = fetch_california_housing()

print(data.feature_names)
print(data.target)  # this is the actual price values, an array
print(data.data.shape)

df = pd.DataFrame(data.data, columns=data.feature_names)
df["Price"] = data.target

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)


winning_pipeline = Pipeline([('scaler', StandardScaler()), ('model', RandomForestRegressor(n_estimators=100, random_state=42))])

winning_pipeline.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error, r2_score

y_pred = winning_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("R2:", r2)