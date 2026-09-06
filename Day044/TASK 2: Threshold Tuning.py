from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

X, y = make_classification(
    n_samples=300,     
    n_features=4,     
    weights=[0.7, 0.3],                     
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=42)
    
model =LogisticRegression(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import roc_curve, auc

proba = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, proba)
roc_auc = auc(fpr, tpr)


from sklearn.metrics import f1_score, precision_score, recall_score

best_f1 = 0
best_thresh = 0.5

best_precision_at_recall = 0
best_thresh_recall85 = None

for thresh in np.arange(0.1, 0.9, 0.05):
    preds = (proba >= thresh).astype(int)
    p = precision_score(y_test, preds)
    r = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    print(f"Thresh: {thresh:.2f} | Precision: {p:.3f} | Recall: {r:.3f} | F1: {f1:.3f}")
    
    if f1 > best_f1:
        best_f1 = f1
        best_thresh = thresh
    
    if r >= 0.85 and p > best_precision_at_recall:
        best_precision_at_recall = p
        best_thresh_recall85 = thresh

print(f"Best F1 threshold: {best_thresh:.2f}, F1: {best_f1:.3f}")
if best_thresh_recall85 is not None:
    print(f"Best precision at recall>=0.85: threshold={best_thresh_recall85:.2f}, precision={best_precision_at_recall:.3f}")
else:
    print("No threshold achieved recall >= 0.85")