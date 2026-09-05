from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(
    n_samples=200,     
    n_features=4,     
    n_informative=3,      
    n_redundant=1,       
    n_classes=2,          
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)

#GB model
model_1 =GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

model_1.fit(X_train, y_train)

y_pred_1 = model_1.predict(X_test)

accuracy_1 = accuracy_score(y_test, y_pred_1)
report_1 = classification_report(y_test, y_pred_1)

print(f"Test Accuracy for gradientmodel: {accuracy_1:.4f}\n")
print("Classification Report for model_1:")
print(report_1) 

#RF model

model_2 =RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)

model_2.fit(X_train, y_train)

y_pred_2 = model_2.predict(X_test)

accuracy_2 = accuracy_score(y_test, y_pred_2)
report_2 = classification_report(y_test, y_pred_2)

print(f"Test Accuracy for RF model: {accuracy_2:.4f}\n")
print("Classification Report for model_2:")
print(report_2)

train_acc_1 = model_1.score(X_train, y_train)
test_acc_1 = model_1.score(X_test, y_test)
gap_1 = train_acc_1 - test_acc_1

train_acc_2 = model_2.score(X_train, y_train)
test_acc_2 = model_2.score(X_test, y_test)
gap_2 = train_acc_2 - test_acc_2

print(f"GB  | Train: {train_acc_1:.3f} | Test: {test_acc_1:.3f} | Gap: {gap_1:.3f}")
print(f"RF  | Train: {train_acc_2:.3f} | Test: {test_acc_2:.3f} | Gap: {gap_2:.3f}")