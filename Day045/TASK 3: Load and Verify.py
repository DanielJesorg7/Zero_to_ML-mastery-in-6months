import joblib
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# Rebuild data + split ONLY (fast, no GridSearchCV needed)
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Price"] = data.target
X = df.drop("Price", axis=1)
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Load the SAME saved model twice — pretend it's "original" and "loaded"
best_model = joblib.load("california_housing_model.joblib")
loaded_model = joblib.load("california_housing_model.joblib")

original_preds = best_model.predict(X_test)
loaded_preds = loaded_model.predict(X_test)

print("Predictions match:", np.array_equal(original_preds, loaded_preds))

new_house = pd.DataFrame({
    'MedInc': [8.0], 'HouseAge': [25], 'AveRooms': [6.0], 'AveBedrms': [1.0],
    'Population': [1200], 'AveOccup': [3.0], 'Latitude': [34.0], 'Longitude': [-118.0]
})
predicted_price = loaded_model.predict(new_house)
print("Predicted price:", predicted_price)