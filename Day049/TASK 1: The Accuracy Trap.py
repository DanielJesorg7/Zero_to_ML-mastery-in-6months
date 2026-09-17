from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=1000, n_features=4, weights=[0.95, 0.05], 
                           n_informative=3, n_redundant=0, random_state=42)
                           
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""
Accuracy is 97.5
It caught 5 out of 9
accuracy is misleading because it's dominated by the majority class.
"""