from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import roc_curve, auc

X, y = make_classification(
    n_samples=300,     
    n_features=4,     
    weights=[0.7, 0.3],                     
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)
    
lr = LogisticRegression(random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
gbc = GradientBoostingClassifier(n_estimators=100, random_state=42)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
gbc.fit(X_train, y_train)

proba_lr = lr.predict_proba(X_test)[:, 1]
proba_rf = rf.predict_proba(X_test)[:, 1]
proba_gbc = gbc.predict_proba(X_test)[:, 1]

fpr_lr, tpr_lr, _ = roc_curve(y_test, proba_lr)
fpr_rf, tpr_rf, _ = roc_curve(y_test, proba_rf)
fpr_gbc, tpr_gbc, _ = roc_curve(y_test, proba_gbc)

auc_lr = auc(fpr_lr, tpr_lr)
auc_rf = auc(fpr_rf, tpr_rf)
auc_gbc = auc(fpr_gbc, tpr_gbc)

print(f"LR AUC: {auc_lr:.3f}")
print(f"RF AUC: {auc_rf:.3f}")
print(f"GBC AUC: {auc_gbc:.3f}")

#no , AUC is one useful signal, not the whole decision