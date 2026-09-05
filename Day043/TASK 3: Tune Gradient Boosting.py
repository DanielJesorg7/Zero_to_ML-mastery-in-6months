from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, StratifiedKFold

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

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', GradientBoostingClassifier(random_state=42))
])

param_grid = {
    'model__learning_rate': [0.01, 0.1, 0.2],
    'model__n_estimators': [50, 100, 200],
    'model__max_depth': [2, 3, 5]
}

grid = GridSearchCV(pipe,param_grid,cv=StratifiedKFold(5, shuffle=True, random_state=42))
grid.fit(X_train,y_train)


grid.best_estimator_.named_steps['model'].feature_importances_

print("Feature importances:", grid.best_estimator_.named_steps['model'].feature_importances_)

print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)
print("Test accuracy:", grid.best_estimator_.score(X_test, y_test))
