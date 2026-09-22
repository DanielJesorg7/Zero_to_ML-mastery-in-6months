from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

import numpy as np
from sklearn.model_selection import validation_curve, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

cv = StratifiedKFold(5, shuffle=True, random_state=42)
param_range = [1, 2, 4, 8, 16, 32]

train_s, val_s = validation_curve(
    RandomForestClassifier(random_state=42), X_train, y_train,
    param_name='max_depth', param_range=param_range,
    cv=cv, scoring='accuracy'
)

train_mean = train_s.mean(axis=1)
val_mean = val_s.mean(axis=1)
for p, tm, vm in zip(param_range, train_mean, val_mean):
    print(f"max_depth={p:<3} train={tm:.3f}  cv={vm:.3f}")
    
"""
Underfits at max depth 1
Over fits at max depth 4
Sweet spot is 8 cos even though 16 and 32 also scored 1 ,8 performed better in the CV by 0.002
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

scaled_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

param_range_c = [0.001, 0.01, 0.1, 1, 10, 100]

train_s_lr, val_s_lr = validation_curve(
    scaled_lr, X_train, y_train,
    param_name='model__C', param_range=param_range_c,
    cv=cv, scoring='accuracy'
)

train_mean_lr = train_s_lr.mean(axis=1)
val_mean_lr = val_s_lr.mean(axis=1)
for c, tm, vm in zip(param_range_c, train_mean_lr, val_mean_lr):
    print(f"C={c:<7} train={tm:.3f}  cv={vm:.3f}")
    
"""The train score keeps as ascending but the CV peaked at 0.1 then reduced, 
Underfit should be 0.001
Overfit should 100, 
Sweet spot is the peak 0.1 ,not always the peak but here I'm this exercise/dataset ,it's the peak

RF is more overfit-prone here because trees can grow arbitrarily complex, while LR's linear boundary structurally limits how far it can drift into memorization.
"""


from sklearn.model_selection import learning_curve

sizes, train_s_lc, val_s_lc = learning_curve(
    scaled_lr, X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=cv, scoring='f1'
)

train_mean_lc = train_s_lc.mean(axis=1)
val_mean_lc = val_s_lc.mean(axis=1)
for s, tm, vm in zip(sizes, train_mean_lc, val_mean_lc):
    print(f"n={s:<4.0f} train={tm:.3f}  cv={vm:.3f}")
   
"""
So I'm answer to the questions
Yeah it flattened out specifically after n =145
And since both train and CV are high -low bias and low variance, I'd say the model is good , 
And surely a good model wouldn't need 5000 rows , it's already good ffs , it's learned already any addition would have a noticeable change on it
"""

sizes_rf, train_s_rf, val_s_rf = learning_curve(
    RandomForestClassifier(n_estimators=100, random_state=42), X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=cv, scoring='f1'
)

train_mean_rf = train_s_rf.mean(axis=1)
val_mean_rf = val_s_rf.mean(axis=1)
for s, tm, vm in zip(sizes_rf, train_mean_rf, val_mean_rf):
    print(f"n={s:<4.0f} train={tm:.3f}  cv={vm:.3f}")
    
    
    """
PRESCRIPTION:

LR: Low bias, low variance - already in the good zone. No fix needed.
Even at the smallest sample sizes tested (n=36-109), LR's train and CV
scores were already high and close together - it doesn't need much
data to behave reliably, because its simple linear structure can't
overfit hard even with little data.

RF: High variance / overfitting - train sits at 1.000 no matter the
data size, and the gap to CV stays wide throughout. Two fixes: (1)
limit max_depth (Task 1 showed depth=8 gives a smaller gap and better
CV than deeper trees), and (2) more data - RF's CV score was still
inching upward at n=364, unlike LR which had already flattened, so
RF is the one model here where "collect more data" is genuinely the
right prescription.

SCENARIO VERDICT:
- Lagos startup (500 rows): LogisticRegression. It was already stable
  and reliable even at the smallest training sizes tested - it doesn't
  need a lot of data to perform well, which is exactly the startup's
  situation.
- Bank (5 million rows): RandomForest. RF is data-hungry and its CV
  score was still climbing at n=364 - a bank's dataset is large enough
  to close that gap and let RF's higher ceiling (able to capture more
  complex patterns than LR's straight line) actually pay off.
"""