

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
from sklearn.model_selection import cross_val_score, GroupKFold, KFold, TimeSeriesSplit, StratifiedKFold
from sklearn.linear_model import LinearRegression



rng = np.random.default_rng(42)

gkf = GroupKFold(n_splits=5)

groups = np.repeat(np.arange(80),7)

patient_offset = rng.normal(0,3,80)
per_row_offset = patient_offset[groups]

X = rng.normal(0,1,(560,5))+per_row_offset[:,None]
y = (X[:,0]+ per_row_offset+rng.normal(0,1,560)>0).astype(int)

pipeline_lr = Pipeline([('scaler', StandardScaler()),
                    ('model',LogisticRegression(max_iter = 1000)) ])

scores_group_lr = cross_val_score(pipeline_lr,X,y,groups= groups, cv = gkf)
print("Scores_group_lr:", scores_group_lr.mean())
stratKFold = StratifiedKFold(5,shuffle=True,random_state=42)
scores_stratKFold_lr = cross_val_score(pipeline_lr,X,y, cv = stratKFold)
print("Scores_stratKFold_lr:", scores_stratKFold_lr.mean())


# GroupKFold answers the new-patient question because the patient record are either in the training set or testing set, no leak between both sets
# In my data, the signal is in the features, so the model didn't need to know the patient..
# That's why the two scores were almost the same: stratified KFold (0.94286) vs Group KFold(0.94107)(0.002 difference )
# With real patients,the quirks don't show in the features, so the random split would be inflated and the gap would grow


from sklearn.ensemble import  RandomForestClassifier
rng = np.random.default_rng(42)

gkf = GroupKFold(n_splits=5)

groups = np.repeat(np.arange(80),7)

patient_offset = rng.normal(0,3,80)
per_row_offset = patient_offset[groups]

X = rng.normal(0,1,(560,5))+per_row_offset[:,None]
y = (X[:,0]+ per_row_offset+rng.normal(0,1,560)>0).astype(int)

pipeline_rf = Pipeline([('scaler', StandardScaler()),
                    ('model',RandomForestClassifier(n_estimators=100, random_state=42)) ])

scores_group_rf = cross_val_score(pipeline_rf,X,y,groups= groups, cv = gkf)
print("Scores_group_rf:", scores_group_rf.mean())
stratKFold = StratifiedKFold(5,shuffle=True,random_state=42)
scores_stratKFold_rf = cross_val_score(pipeline_rf,X,y, cv = stratKFold)
print("Scores_stratKFold_rf:", scores_stratKFold_rf.mean())


t = np.arange(200).reshape(-1,1)
y_time = 2 * t.ravel()+ rng.normal(0,5,200)

tkf = KFold(5,shuffle=True,random_state=42)
scores_tkf_lr = cross_val_score(LinearRegression(),t,y_time, cv = tkf,scoring="r2")
print("Scores_tkf_lr:", scores_tkf_lr.mean())

tss = TimeSeriesSplit(n_splits=5)
scores_tss_lr = cross_val_score(LinearRegression() ,t,y_time, cv = tss,scoring="r2")
print("Scores_tss_lr:", scores_tss_lr.mean())


# 1. Shuffled KFold: The model may train on observations that occur after a validation observation.
# TimeSeriesSplit: The model trains on earlier observations and validates on later ones
# Hence Time series Split is the right CV for this model
# 2. In shuffled KFold, a validation point can have training observations from both its past and its future whereas a real future point only has historical observations available.
# 3. Because  the underlying trend is simple and stable, linear regression model , it doesn't need much data to figure out it's general trajectory idk 😐


# A. GroupKFold definitely, it ensures if a patient's record is in training it won't be in testing, to prevent data leakages
# B. Model with TimeSeriesSplit , for obvious reasons, it's principle;"reproduce the intended prediction conditions as faithfully as practical."
# C. Stratified KFold CV works here as the data is Independent, and no group overlapping, Group KFold can work too but it's not  necessar


# 1. Interpolation, ' cos it's "inside"  the available data
# 
# 
# 2. Extrapolation, ' cos it's outside" the available data
# 
# 
# 3. The correct CV to be used is Time Series Split, shuffling is a bad idea 'cos you're not predicting records in the past, IT'S A FREAKING TIME SERIES AND MY COLLEAGUE SHOULD KNOW BETTER! you're predicting the future based on past data
