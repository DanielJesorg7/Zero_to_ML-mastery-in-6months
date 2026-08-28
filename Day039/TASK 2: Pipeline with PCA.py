import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=200, n_features=4, n_classes=2,
                           n_informative=3, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline2 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('model', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))
])

pipeline2.fit(X_train, y_train)
predictions2 = pipeline2.predict(X_test)
print("Task 2 accuracy:", accuracy_score(y_test, predictions2))
print("Named steps:", pipeline2.named_steps)
print("Explained variance ratio:", pipeline2.named_steps['pca'].explained_variance_ratio_)
print("Feature importances:", pipeline2.named_steps['model'].feature_importances_)