from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, random_state=42)
X[:, 0] = X[:, 0] * 1000000
X[:, 1] = X[:, 1] * 10

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_bad = SVC(kernel="linear", random_state=42)
svm_bad.fit(X_train, y_train)
print("NO scaling accuracy:", svm_bad.score(X_test, y_test))

scaler = StandardScaler()
X_train_good = scaler.fit_transform(X_train)
X_test_good = scaler.transform(X_test)

svm_good = SVC(kernel="linear", random_state=42)
svm_good.fit(X_train_good, y_train)
print("WITH scaling accuracy:", svm_good.score(X_test_good, y_test))