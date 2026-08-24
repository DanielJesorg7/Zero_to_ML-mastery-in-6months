import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)
n = 400

data = {
    "years_at_company": np.random.randint(1, 15, n),
    "performance_rating": np.random.uniform(2.0, 5.0, n),
    "projects_completed": np.random.randint(3, 30, n),
    "salary": np.random.randint(200000, 1500000, n),
    "training_hours": np.random.randint(10, 100, n)
}
df = pd.DataFrame(data)

df["promoted"] = np.where(
    (df["performance_rating"] > 3.8) & (df["projects_completed"] > 15) & (df["years_at_company"] > 3),
    1, 0
)

X = df.drop("promoted", axis=1)
y = df["promoted"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel="rbf", random_state=42)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

new_employee = [[7, 4.2, 20, 800000, 45]]
new_employee_scaled = scaler.transform(new_employee)
prediction = model.predict(new_employee_scaled)
print("Promotion prediction (1=yes, 0=no):", prediction)