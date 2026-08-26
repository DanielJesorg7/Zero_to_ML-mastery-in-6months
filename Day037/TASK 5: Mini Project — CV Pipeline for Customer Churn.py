import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)
n_rows = 400

# 1. Build the features
data = {
    'tenure': np.random.randint(1, 61, size=n_rows),                  # 1 to 60 months
    'monthly_charges': np.random.randint(1000, 20001, size=n_rows),  # 1,000 to 20,000
    'support_calls': np.random.randint(0, 11, size=n_rows),           # 0 to 10 calls
    'contract_type': np.random.choice([1, 12, 24], size=n_rows)       # 1, 12, or 24 months
}

df = pd.DataFrame(data)

# 2. Apply your conditional target logic
df['churn'] = (
    (df['monthly_charges'] > 12000) & 
    (df['tenure'] < 12) & 
    (df['support_calls'] > 5) & 
    (df['contract_type'] == 1)
).astype(int)

df_encoded = pd.get_dummies(df, columns=["contract_type"])

# Convert boolean True/False to 1/0 integers for the new columns
contract_cols = [col for col in df_encoded.columns if "contract_type" in col]
df_encoded[contract_cols] = df_encoded[contract_cols].astype(int)

X = df_encoded.drop("churn", axis=1)
y = df_encoded["churn"]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)   # OK to fit on full X here — CV handles splitting internally

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "SVM (RBF)": SVC(kernel="rbf", random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=6, random_state=42)
}

for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=skf)
    print(f"{name}")
    print("  Mean:", scores.mean(), "Std:", scores.std())
    
    
    
    
# Random Forest has the highest mean CV accuracy (0.9925), but the margin
# over Logistic Regression (0.9875) is small (~0.5%) and Random Forest has
# the highest std (least consistent across folds). On data this clean and
# rule-based, all three models perform excellently — Random Forest's edge
# here is marginal, not decisive. In practice, Logistic Regression's near-
# identical accuracy with a simpler, more interpretable model could make it
# the more practical choice depending on business needs.