import numpy as np
from sklearn.datasets import  load_breast_cancer
from sklearn.model_selection import train_test_split


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

import matplotlib.pyplot as plt


data = load_breast_cancer()
X,y = data.data,data.target
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size = 0.2, random_state = 42,stratify=y )

cv = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)


C_Values = [0.01,0.1,1,10,100]

for C in (C_Values):                    # start strong (small C), relax
    
    pipe = Pipeline([
        ('scaler',StandardScaler()),
        ('model', LogisticRegression(penalty='l1', solver='liblinear', C=C, max_iter=1000))
    ])        

    scores = cross_val_score(pipe,X_train,y_train,cv=cv,scoring='f1')


    pipe.fit(X_train,y_train)

    survivor_count = np.sum(pipe.named_steps['model'].coef_ !=0)
    print(C,survivor_count,scores.mean())


# Task 1 output and comment
 

#0.01	3	0.9328
#0.1	8	0.9714
#1	    16	0.9719
#10 	22	0.9612
#100	25	0.9596
 
# # TASK 1 COMMENT

# As C increases from 0.01 to 100, regularization becomes weaker, giving the model more freedom to retain features. We can see the number of surviving features increase from 3 to 25.

# The highest CV F1 score is 0.9719 at C = 1, with 16 surviving features. At C = 0.1, only 8 features survive, yet the score is almost identical (0.9714). This suggests that the model can achieve similar performance with fewer features.

# When C is reduced to 0.01, regularization becomes too strong for this experiment: only 3 features survive and CV F1 drops to 0.9328. On the other hand, increasing C beyond 1 also reduces the CV score slightly.

# This demonstrates the trade-off between model complexity and performance: retaining more features does not automatically improve the model.

# 8 features achieved almost the same CV score as 16

scaler  = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

C_Values = [0.001,0.01,0.1,1,10,100]
coef_paths = {name : [] for name in data.feature_names}

for C in C_Values:
    model_LR = LogisticRegression(penalty='l1',solver='liblinear',C=C,max_iter=1000)
    model_LR.fit(X_train_scaled,y_train)

    for j,name in enumerate(data.feature_names):
        coef_paths[name].append(model_LR.coef_[0][j])

    survivor_count2 = np.sum(model_LR.coef_ !=0)
    print(C,survivor_count2)

for name in data.feature_names:
    if coef_paths[name][1]!=0:
        print(name)


# TASK 2 COMMENT 
# Features surviving at C = 0.01
# 3 / 30
# - Worst radius
# - Worst perimeter
# - Worst concave points
 
 
# Day 53 asked: Which features influence the model's predictions?
# Day 59 asks: Which features can remain in the model when we penalize complexity?

plt.figure()
for name in data.feature_names:
    if coef_paths[name][1]!=0:
        plt.plot(range(len(C_Values)), coef_paths[name], marker='o', label=name)
plt.xlabel('regularization strength →'); plt.ylabel('coefficient size')
plt.xticks(range(len(C_Values)), C_Values)
plt.legend(); plt.savefig('coef_path.png', bbox_inches='tight')


Cs = [0.001, 0.01, 0.1, 1, 10, 100]
l1_scores = []
l2_scores = []

for C in Cs:
    pipe_l1 = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(penalty='l1', solver='liblinear', C=C, max_iter=1000))
    ])
    pipe_l2 = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(C=C, max_iter=1000))
    ])

    s1 = cross_val_score(pipe_l1, X_train, y_train, cv=cv, scoring='f1').mean()
    s2 = cross_val_score(pipe_l2, X_train, y_train, cv=cv, scoring='f1').mean()

    l1_scores.append(s1)
    l2_scores.append(s2)

print([round(float(s), 4) for s in l1_scores])
print([round(float(s), 4) for s in l2_scores])

plt.figure()
plt.plot(range(len(Cs)), l1_scores, marker='o', label='L1')
plt.plot(range(len(Cs)), l2_scores, marker='o', label='L2')
plt.xticks(range(len(Cs)), Cs)
plt.xlabel('C (small = strong penalty)')
plt.ylabel('CV F1')
plt.legend()
plt.savefig('l1_curve.png', bbox_inches='tight')
plt.show()

best_c_l1 = Cs[np.argmax(l1_scores)]
best_c_l2 = Cs[np.argmax(l2_scores)]

print("L1 best C:", best_c_l1, "CV F1:", max(l1_scores))
print("L2 best C:", best_c_l2, "CV F1:", max(l2_scores))


from sklearn.metrics import f1_score

best_l1_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(
        penalty='l1',
        solver='liblinear',
        C=best_c_l1,
        max_iter=1000
    ))
])

best_l1_pipe.fit(X_train, y_train)

l1_predictions = best_l1_pipe.predict(X_test)

print("L1 Test F1:", f1_score(y_test, l1_predictions))



best_l2_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(
        penalty='l2',
        C=best_c_l2,
        max_iter=1000
    ))
])

best_l2_pipe.fit(X_train, y_train)

l2_predictions = best_l2_pipe.predict(X_test)

print("L2 Test F1:", f1_score(y_test, l2_predictions))

# TASK 3 OUTPUT
 
# L1 best C: 1 CV F1: 0.9736003426858
# L2 best C: 0.1 CV F1: 0.9861164154764722
# L1 Test F1: 0.993103448275862
# L2 Test F1: 0.9793103448275862
 
 
# TASK 3 COMMENT
# L2 won cross-validation by approximately 0.0125 (1.25 percentage points).
 
# L1 won on the held-out test set by approximately 0.0138 (1.38 percentage points)
 
# Well the model that wins cross-validation doesn't necessarily win on one particular test split. The test result is useful, but one split doesn't prove L1 is universally better. Different samples can produce different results


# TASK 4 INTERVIEW VERDICT
# 1. L1 essentially eliminates features whose coefficients have been shrunk down to zero(feature selection), useful when many features may be irrelevant (removes features that might not be needed),L2 generally shrinks coefficient towards zero , generally retains features and useful when many features carry signal including correlated ones (reduces how heavily we depend on certian features)
# 2. L1 definitely reasons above
# 3. L2 ,reasons above
# 4. Day 52 taught me how to diagnose model complexity; Day 59 gives me a way to control it by adjusting C value (regularization low value; 0.001 means stronger regularization, high value; 100 means weaker regularization)
