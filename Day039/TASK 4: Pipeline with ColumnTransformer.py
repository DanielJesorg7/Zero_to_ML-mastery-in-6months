import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)
n4 = 300

data4 = {
    "age": np.random.randint(18, 66, n4),
    "income": np.random.randint(100000, 2000001, n4),
    "tenure": np.random.randint(1, 61, n4),
    "department": np.random.choice(['Sales', 'Engineering', 'HR', 'Marketing'], n4),
    "level": np.random.choice(['Junior', 'Senior', 'Lead'], n4)
}
df4 = pd.DataFrame(data4)
df4["promoted"] = np.where(
    (df4["income"] > 800000) & (df4["tenure"] > 3) & (df4["level"] == 'Senior'),
    1, 0
)

numeric_features = ['age', 'income', 'tenure']
categorical_features = ['department', 'level']

preprocessor4 = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

pipeline4 = Pipeline([
    ('preprocessor', preprocessor4),
    ('model', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))
])

X4 = df4.drop("promoted", axis=1)
y4 = df4["promoted"]
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y4, test_size=0.2, random_state=42)

pipeline4.fit(X4_train, y4_train)
predictions4 = pipeline4.predict(X4_test)
print("Task 4 accuracy:", accuracy_score(y4_test, predictions4))

new_employee = pd.DataFrame({
    "age": [30], "income": [900000], "tenure": [5],
    "department": ['Engineering'], "level": ['Senior']
})
print("New employee prediction:", pipeline4.predict(new_employee))