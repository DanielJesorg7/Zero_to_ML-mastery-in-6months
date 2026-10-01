from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd

data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

importances = model.feature_importances_



top = pd.Series(importances, index=data.feature_names).sort_values(ascending=False)
print(top.head(10))

"""
The top features are mostly the “worst” measurements (area, concave points, radius).
These make medical sense because they describe the most abnormal-looking cells.
Larger, more irregular cells are typical signs doctors associate with malignancy.
"""

from sklearn.inspection import permutation_importance

result = permutation_importance(
    model, X_test, y_test,
    n_repeats=10,
    random_state=42
)


top_perm = pd.Series(result.importances_mean, index=data.feature_names).sort_values(ascending=False)
print(top_perm.head(10))


"""
1. "worst area," "mean concave points," "mean area," "mean radius," "mean concavity" are in both lists
2. Worst concave and worst radius (0.13 and 0.098)
3. Radius, perimeter and area are describing the same thing ,so shuffling through them barely hurts the accuracy,as inbuilt importance just checks usage counts in tree structure not result after removal
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaled_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])
scaled_lr.fit(X_train, y_train)
coefs = scaled_lr.named_steps['model'].coef_[0]
top_coefs = pd.Series(coefs, index=data.feature_names).sort_values(ascending=False)
print("Pushes toward BENIGN (positive):\n", top_coefs.head(5))
print("Pushes toward MALIGNANT (negative):\n", top_coefs.tail(5))

"""
Scaling puts every feature on the same unit(mean 0 and std 1)so 1 unit change is uniform across all features for honest comparison as some features are usually relatively big (e.g age and salary)
"""

from sklearn.tree import DecisionTreeClassifier, export_text

shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
shallow.fit(X_train, y_train)
print(export_text(shallow, feature_names=list(data.feature_names)))

from sklearn.metrics import accuracy_score
shallow_acc = accuracy_score(y_test, shallow.predict(X_test))
rf_acc = accuracy_score(y_test, model.predict(X_test))
print("Shallow tree accuracy:", shallow_acc)
print("RF accuracy:", rf_acc)



"""
Verdict: deploy (b), the shallow transparent tree.

RF + permutation importance tells you which features matter in general,
across the whole dataset - it can't give a specific customer a reason
for THEIR rejection. The shallow tree (max_depth=3) gives an exact,
readable path: "worst radius > 16.80, texture error > 0.47, worst
concavity > 0.19 -> rejected." That's something a loan officer can
explain in plain language, and something a regulator can audit.

Tradeoff: the shallow tree scored 0.939 accuracy vs RF's 0.956 on the
test set - a measured gap of about 1.8 percentage points, not a guess.
Small enough that trading it for a fully explainable, per-case decision
path is an easy call. For a decision that legally requires an
explanation (loan rejections), an explainable model you can defend
beats a slightly more accurate one you can't.
"""