from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression


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

print(f"AUC: {roc_auc:.3f}")

#mathplotlip keeps crashing pydriod 