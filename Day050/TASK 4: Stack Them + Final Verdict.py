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

from sklearn.ensemble import StackingClassifier

stacking = StackingClassifier(
    estimators=[
        ('lr', LogisticRegression(max_iter=1000)),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gb', GradientBoostingClassifier(random_state=42))
    ],
    final_estimator=LogisticRegression(max_iter=1000),
    cv=5
)
stacking.fit(X_train, y_train)
y_pred_stack = stacking.predict(X_test)

print("Accuracy _stack:", accuracy_score(y_test, y_pred_stack))
print("Confusion Matrix  :\n", confusion_matrix(y_test, y_pred_stack))
print("Classification Report  :\n", classification_report(y_test, y_pred_stack))

from sklearn.metrics import f1_score
print("F1 stack:", f1_score(y_test, y_pred_stack))

"""
Final verdict: I would deploy solo LogisticRegression.

It's tied for the best accuracy (0.9649) and F1 (0.97) of all 6 models,
using a single model that's fast to train, cheap to run, and easy to
explain to a non-technical stakeholder or auditor.

Hard voting matched LR's score exactly but requires training and 
maintaining 3 models instead of 1, for zero actual gain here.

Soft voting and stacking both scored WORSE than solo LR (0.9561 vs 0.9649)
despite being far more complex - stacking alone runs 4 models total
(3 base + 1 meta-learner) with internal cross-validation. More machinery
did not mean better results on this dataset.

Principle: added complexity has to earn its place with a measurable gain.
Here it didn't - so the simplest model that hits the top score wins.
""""