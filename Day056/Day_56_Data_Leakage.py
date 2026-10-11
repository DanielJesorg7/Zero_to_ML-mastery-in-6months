

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



rng = np.random.default_rng(42)
leaky_train = np.column_stack([X_train,y_train + rng.normal(0,0.1,len(y_train))])
leaky_test = np.column_stack([X_test,y_test + rng.normal(0,0.1,len(y_test))])


leaky_scores = cross_val_score(baseline_lr,leaky_train,y_train,cv=cv,scoring = 'f1')
print("Leaky CV F1:",leaky_scores.mean())


clean_scores = cross_val_score(baseline_lr,X_train,y_train,cv=cv,scoring="f1")
print("Clean CV F1:",clean_scores.mean())


# The Leaky Score (0.9982) was near perfect, an relatively high inflation form the baseline score (clean score- 0=9825),a very high score(near perfect score )is an indicator of data leakege though not a confirmation, The hospital should check the entire process (An audition) check should include model's access to features that is the prediction in disguise (target leak),outliers and preprocesses that shares statistic properties with other rows(preprocessing leak) ,if the dataset contains duplicate record (record in both training and test data)(I.e split leakege/train-test contamination)


baseline_scores_t2 = cross_val_score(baseline_lr,X_train,y_train,cv=cv,scoring="f1")
print("Baseline CV F1:",baseline_scores_t2.mean())


scaler_leak = StandardScaler()
X_all_scaled =scaler_leak.fit_transform(X) #This fits all, both test and training rows

X_leak_tr,X_leak_te,y_leak_tr,y_leak_te = train_test_split(X_all_scaled,y, test_size = 0.2, random_state = 42,stratify=y )

plain_lr = LogisticRegression(max_iter = 1000)
leaky_scores_t2 = cross_val_score(plain_lr,X_leak_tr,y_leak_tr,cv=cv,scoring="f1")
print("Leaky (fit-before split) CV F1:",leaky_scores_t2.mean())


# The prepocessing leakage(mean,std) is hardly noticeble on large dataset ,i.e an invisble leak (as the mean/std barely shifts when you add a small percentage more rows to an already stable estimate), therfore makes one undermine the discipline of the pipeline,if the dataset is small and the data contains an extreme value, the leakage becomes much more conpiscous


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rf_clean = RandomForestClassifier(n_estimators=100,random_state=42)
rf_clean.fit(X_train,y_train)
clean_acc = accuracy_score(y_test,rf_clean.predict(X_test))
print("Clean test accuracy:", clean_acc)


rng = np.random.default_rng(42)
dup_idx = rng.choice(len(X_test),size=int(0.3*len(X_test)),replace=False)

X_contam = np.vstack([X_train,X_test[dup_idx]])
y_contam = np.concatenate([y_train,y_test[dup_idx]])

rf_contam = RandomForestClassifier(n_estimators=100,random_state=42)
rf_contam.fit(X_contam,y_contam)
contam_acc = accuracy_score(y_test,rf_contam.predict(X_test))
print("Contaminated test accuracy:", contam_acc)


# Clean test accuracy (0.9561403508877193)
# Contaminated test accuracy (0.964912280701544)
# The inflation is quite obvious here ,some of the test data was injected leaked into the training data so the model "memoried" that particular set of data , that test data was duplicate into the training data
# In practice this wouldn't come from code ; it could happen through a hospital's database migration merging old and new patient record systems without deduplicating, or a patient being registered under two different ID numbers after visiting two different clinics within the same hospital network, silently creating two 'different' rows that are actually the same person


# My audit checklist
# 1. The model is not fed the wrong data at the wrong time(incase of a loan model, data before the loan credit score,income)would suffice, data from after the loan (date due) wouldn't be necessary),DEFINE THE PREDICTION MOMENT
# 2. When using shared statistics values (mean and std) I'd use a pipeline to prevent data leaks (preprocessing leakage)FIT PREPOCESSING OB TRAINING DATA ONLY
# 3. De-duplication if records to prevent ghost leakege
# 4. Cross check the Dataset to prevent predictions disguised as feature, WATCH FOR TARGET PROXIES
# 5. Thorough audition of dataset and model especially after an unusually high accuracy or CV score
# 6. MATCH YOUR SPLIT TO DEPLOYMENT e.g time or gender
# 
# 0.9997 is an unusually high score, I'd tell em ,that and advise to check out for data leakage especially prediction disguised as features
# 
