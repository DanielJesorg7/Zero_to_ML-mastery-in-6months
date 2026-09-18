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

voting_soft = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression(max_iter=1000)),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gb', GradientBoostingClassifier(random_state=42))
    ],
    voting='soft'
)
voting_soft.fit(X_train, y_train)
y_pred_soft = voting_soft.predict(X_test)


print("Accuracy _soft:", accuracy_score(y_test, y_pred_soft))
print("Confusion Matrix  :\n", confusion_matrix(y_test, y_pred_soft))
print("Classification Report  :\n", classification_report(y_test, y_pred_soft))

from sklearn.metrics import f1_score
print("F1 soft:", f1_score(y_test, y_pred_soft))

"""
1. Soft voting can outperform hard voting because it doesn't just look at 
each model's final label — it averages their actual predicted probabilities. 
A model that's 51% confident and a model that's 99% confident get treated 
very differently, so a strongly confident correct prediction can outweigh 
a weakly confident wrong one. Hard voting throws that confidence info away 
and just counts votes equally.

2. On this run, hard voting actually won (0.9649 accuracy, F1 0.9726) 
over soft voting (0.9561 accuracy, F1 0.9660) - the opposite of what the 
theory predicts. Likely reason: LR didn't fully converge (ConvergenceWarning), 
so its probability estimates may be less reliable/calibrated than a clean 
majority vote would need. Soft voting is only better when all models' 
probabilities are trustworthy - here averaging in a shaky probability 
estimate may have dragged the ensemble down instead of helping it.
"""