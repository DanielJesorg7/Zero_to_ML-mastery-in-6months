import joblib 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np


data = fetch_california_housing()

print(data.feature_names)
print(data.target)  # this is the actual price values, an array
print(data.data.shape)

df = pd.DataFrame(data.data, columns=data.feature_names)
df["Price"] = data.target

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)

pipeline = Pipeline([('scaler', StandardScaler()), ('model', GradientBoostingRegressor(random_state=42))])

param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [3, 5]
}
grid = GridSearchCV(pipeline, param_grid, cv=3, scoring='r2')

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

from sklearn.metrics import mean_absolute_error, r2_score

y_pred = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MAE:", mae)
print("R2:", r2)

print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)

joblib.dump(best_model, "gb_housing_model.joblib")


# Load the SAME saved model twice — pretend it's "original" and "loaded"
best_model = joblib.load("gb_housing_model.joblib")
loaded_model = joblib.load("gb_housing_model.joblib")

original_preds = best_model.predict(X_test)
loaded_preds = loaded_model.predict(X_test)

print("Predictions match:", np.array_equal(original_preds, loaded_preds))

new_house = pd.DataFrame({
    'MedInc': [8.0], 'HouseAge': [25], 'AveRooms': [6.0], 'AveBedrms': [1.0],
    'Population': [1200], 'AveOccup': [3.0], 'Latitude': [34.0], 'Longitude': [-118.0]
})
predicted_price = loaded_model.predict(new_house)
print("Predicted price:", predicted_price)

print("Daniel second saved model is successful")


# HOW A TEAMMATE WOULD USE THIS SCRIPT:
# 1. They need the file "gb_housing_model.joblib" in the same directory.
# 2. Load it with: loaded_model = joblib.load("gb_housing_model.joblib")
# 3. New data must be a DataFrame with these exact 8 columns, in this order:
#    MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
# 4. Call loaded_model.predict(new_data) to get predicted prices (in $100,000s).
#I probably should get it licensed so Tom, Dick amd Harry wont just use it anyhow