import joblib 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split,GridSearchCV
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

pipeline = Pipeline([('scaler', StandardScaler()), ('model', RandomForestRegressor( random_state=42))])

param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [10, 20, None],
}
grid = GridSearchCV(pipeline, param_grid, cv=3, scoring='neg_mean_absolute_error')

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

joblib.dump(best_model, "california_housing_model.joblib")

print("Daniel first saved model is successful")
