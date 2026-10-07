
import shap



from sklearn.datasets import  load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestClassifier
import pandas as pd
import numpy as np


data = load_breast_cancer()
X,y = data.data,data.target
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size = 0.2, random_state = 42,stratify=y)


rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_test)

print(rf.classes_)
print(type(shap_values))
print(np.array(shap_values).shape if not isinstance(shap_values, list) else len(shap_values))


# class 1 (benign) SHAP values — note the [:, :, 1] instead of [1]
shap_class1 = shap_values[:, :, 1]

mean_shap = np.abs(shap_class1).mean(axis=0)
top_shap = pd.Series(mean_shap, index=data.feature_names).sort_values(ascending=False)
print(top_shap.head(10))


malignant_idx = np.where(y_test == 0)[0][0]
patient_shap = shap_values[malignant_idx, :, 1]
patient_vals = X_test[malignant_idx]

patient_series = pd.Series(patient_shap, index=data.feature_names).sort_values(ascending=False)

print("Pushed toward BENIGN:\n", patient_series.head(5))
print("\nPulled toward MALIGNANT:\n", patient_series.tail(5))



# in summary "Your scan showed usually large abnormal looking cells,  a major finding, and that mattered a lot more than the few normal-looking signs we also saw"


benign_idx = np.where(y_test == 1)[0][0]
patient_shap_b = shap_values[benign_idx, :, 1]
patient_series_b = pd.Series(patient_shap_b, index=data.feature_names).sort_values(ascending=False)
print("Pushed toward BENIGN:\n", patient_series_b.head(5))
print("\nPulled toward MALIGNANT:\n", patient_series_b.tail(5))



# For this, benign patient the same feature that played a role in determining the last patient as a malignant is exonerating this patient from that fate, showing that features aren't inherently benign or malignant, "what determines the direction is where THIS patient's actual value falls , on the dangerous side of the model's learned split points, or the safe side, global importance shows the worst area mattered in general not which direction it points for a specific person


print("Baseline (average predicted probability of class 1 / benign):", explainer.expected_value[1])


# Final verdict 
# SHAP would be the right upgrade as it is able to tell you why a certain feature means something different from this to that patient, same as shallow but preserving the accuracy of permutation importance, its limitation includes slow computing speed, " independence assumption" problem when correlated it meets correlated features (area, perimeter, radius) it can struggle to separate cleanly between them like permutation importance.
# Before looking at any specific patient's features, the model's default guess is about 63% benign,this is the starting point every patient's SHAP values push or pull away from

