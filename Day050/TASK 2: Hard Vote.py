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

from sklearn.ensemble import VotingClassifier

voting_hard = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression(max_iter=1000)),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gb', GradientBoostingClassifier(random_state=42))
    ],
    voting='hard'
)
voting_hard.fit(X_train, y_train)
y_pred_hard = voting_hard.predict(X_test)


print("Accuracy _hard:", accuracy_score(y_test, y_pred_hard))
print("Confusion Matrix  :\n", confusion_matrix(y_test, y_pred_hard))
print("Classification Report  :\n", classification_report(y_test, y_pred_hard))

from sklearn.metrics import f1_score
print("F1 hard:", f1_score(y_test, y_pred_hard))

"""
1. Yeah by 0.0026 on Class 1 
2. voting only helps as much as the models disagree
"""