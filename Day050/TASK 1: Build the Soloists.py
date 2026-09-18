from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = data.data, data.target
                           
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

modellr = LogisticRegression(max_iter=1000)
modellr.fit(X_train,y_train)

y_predlr = modellr.predict(X_test)

print("Accuracy lr:", accuracy_score(y_test, y_predlr))
print("Confusion Matrix lr :\n", confusion_matrix(y_test, y_predlr))
print("Classification Report lr :\n", classification_report(y_test, y_predlr))


modelrf = RandomForestClassifier(n_estimators=100, random_state=42)
modelrf.fit(X_train,y_train)

y_predrf = modelrf.predict(X_test)

print("Accuracy rf:", accuracy_score(y_test, y_predrf))
print("Confusion Matrix rf :\n", confusion_matrix(y_test, y_predrf))
print("Classification Report rf :\n", classification_report(y_test, y_predrf))


modelgb = GradientBoostingClassifier(random_state=42)
modelgb.fit(X_train,y_train)

y_predgb = modelgb.predict(X_test)

print("Accuracy gb:", accuracy_score(y_test, y_predgb))
print("Confusion Matrix gb:\n", confusion_matrix(y_test, y_predgb))
print("Classification Report gb:\n", classification_report(y_test, y_predgb))


"""
Yes — LR, by accuracy (0.965 vs 0.956 for both RF and GB)
"""