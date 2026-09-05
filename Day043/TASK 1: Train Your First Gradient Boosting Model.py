from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

X, y = make_classification(
    n_samples=200,     
    n_features=4,     
    n_informative=3,      
    n_redundant=1,        #explain fbis very well please
    n_classes=2,          
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)
    
model =GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(report) 