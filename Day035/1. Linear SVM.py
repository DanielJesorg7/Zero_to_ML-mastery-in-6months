from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=200, n_features=2, n_classes=2,
                           n_informative=2, n_redundant=0, n_clusters_per_class=1,
                           random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel="linear", random_state=42)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
