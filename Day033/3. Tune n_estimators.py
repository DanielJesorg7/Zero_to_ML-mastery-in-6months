from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=200, n_features=4, n_classes=2,
                           n_informative=3,n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# Decision Tree (same max_depth)
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

# Random Forest (same max_depth per tree)
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

print("Decision Tree | Train:", dt.score(X_train, y_train), "| Test:", dt.score(X_test, y_test))
print("Random Forest | Train:", rf.score(X_train, y_train), "| Test:", rf.score(X_test, y_test))

for n in [10, 50, 100, 200, 500]:
    model = RandomForestClassifier(n_estimators=n, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    print(f"n_estimators={n:3d} | Test Accuracy: {test_acc:.4f}")
