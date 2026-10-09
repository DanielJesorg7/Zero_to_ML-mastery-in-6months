import pandas as pd
import numpy as np
from sklearn.datasets import  load_breast_cancer
from sklearn.model_selection import train_test_split



data = load_breast_cancer()
X,y = data.data,data.target
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size = 0.2, random_state = 42,stratify=y )



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score,StratifiedKFold

cv = StratifiedKFold(5,shuffle=True,random_state=42)

baseline_lr = Pipeline([
    ('scaler',StandardScaler()),
    ('model', LogisticRegression(max_iter = 1000))
])
baseline_scores = cross_val_score(baseline_lr,X_train,y_train,cv=cv,scoring="f1")
print("Baseline CV F1:",baseline_scores.mean())


from sklearn.preprocessing import PolynomialFeatures

interaction_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2,interaction_only=True,include_bias=False)),
    ('model',LogisticRegression(max_iter=1000))
])
interaction_scores = cross_val_score(interaction_lr,X_train,y_train,cv=cv,scoring='f1')
print("Interaction CV F1:",interaction_scores.mean())


print("Original features", X_train.shape[1])
interaction_lr.fit(X_train,y_train)
n_poly_features = interaction_lr.named_steps['poly'].transform(interaction_lr.named_steps['scaler'].transform(X_train)).shape[1]
print("After interaction", n_poly_features)


# The model didnt learn anything new  as it had alreadly learnt all from the previous dataset, as day 52, the curve's flattened out, in this case, the column is now more than the rows so the model fits in noise, hence the drop in CV, the extra 435 column did mor eharm than good in this case


from sklearn.preprocessing import KBinsDiscretizer

binned_lr = Pipeline([
    ('binner', KBinsDiscretizer(n_bins=5, encode='onehot',strategy=('quantile'))),
    ('model',LogisticRegression(max_iter=1000))
])
binned_scores = cross_val_score(binned_lr,X_train,y_train,cv=cv,scoring='f1')
print("binned CV F1:",binned_scores.mean())


# Binning converts one continous number into multiple independentbyes/no buckets, which let a linear model assign different weight to each range which is impossible with a straight line as it has only a constant slop, this can therefore capture non monotonic patterns(risky at the middle and safe at the end). In this case it(0.9756) performed better than interactive_lr(0.9700) but slightly worse than the baseline(0.9825) as relationship here had no hidden curves to rescue  as they were apparently already close to linear, "binnning threw away the precise number value without matching benefit "


X_train_df = pd.DataFrame(X_train, columns = data.feature_names)
X_test_df = pd.DataFrame(X_test, columns = data.feature_names)




X_train_df['roundness'] = (X_train_df["mean perimeter"]**2)/X_train_df['mean area']
X_test_df['roundness'] = (X_test_df["mean perimeter"]**2)/X_test_df['mean area']


roundness_lr = Pipeline([
    ('scaler',StandardScaler()),
    ('model', LogisticRegression(max_iter = 1000))
])
roundness_scores = cross_val_score(roundness_lr,X_train_df,y_train,cv=cv,scoring="f1")
print("Roundness CV F1:",roundness_scores.mean())


# # Roundness_lr (0.98258) actually edges out baseline_lr (0.98254) by a tiny 
# margin - a genuine measured improvement, though very small. This feature 
# measures cell irregularity: high roundness = jagged/irregular shape, often 
# malignant; a perfect circle has the minimum possible value. It shows that 
# one line of domain knowledge can match or slightly beat 435 brute-force 
# interaction features - understanding the problem beats throwing raw 
# computation at it.

print("Baseline LR:",baseline_scores.mean())
print("Interaction LR:",interaction_scores.mean())
print("Binned LR:",binned_scores.mean())
print("Roundness LR:",roundness_scores.mean())

"""
VERDICT — four feature factories compared (CV F1):
Baseline 0.9825 | Interaction 0.9701 | Binned 0.9756 | Roundness 0.9826

When to reach for each:
- Interactions (PolynomialFeatures): skip when rows are limited and the 
  model is already near its ceiling - here it added 435 noisy columns to 
  ~455 rows and actively hurt performance. Only worth trying when you 
  genuinely suspect feature interactions matter AND have enough data to 
  support the extra columns.
- Bins (KBinsDiscretizer): useful when a relationship is non-monotonic 
  (risky in the middle, safe at the extremes) and you're stuck with a 
  linear model. Here the relationships were already close to linear, so 
  binning just threw away precision for no benefit.
- Domain features (roundness): the best return on effort today - one line 
  of real domain knowledge tied/slightly beat 435 brute-force features. 
  Reach for this first, always, before brute-force generation.

Revisiting Day 52's "high bias -> add features" prescription:
Day 52's LR curve showed both train and CV high and close together - 
that's the 'ship it' shape, not high bias. There was no bias problem to 
fix in the first place. So today's result makes sense: adding 435 
brute-force features didn't help because 'add more features' only works 
when the diagnosis is actually high bias - applying it blindly, without 
checking the real diagnosis first, just added noise to an already-good 
model.
"""