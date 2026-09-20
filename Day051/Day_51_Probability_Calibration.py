# Day 51: Probability Calibration

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import brier_score_loss
from sklearn.calibration import CalibratedClassifierCV

# --- Data (loaded once) ---
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- Task 1: Reproduce the crime scene ---
modellr = LogisticRegression(max_iter=1000)
modellr.fit(X_train, y_train)
proba_lr = modellr.predict_proba(X_test)[:, 1]
brier_lr = brier_score_loss(y_test, proba_lr)

modelrf = RandomForestClassifier(n_estimators=100, random_state=42)
modelrf.fit(X_train, y_train)
proba_rf = modelrf.predict_proba(X_test)[:, 1]
brier_rf = brier_score_loss(y_test, proba_rf)

# Unscaled LR had the more honest probabilities (lower Brier) than RF,
# even though LR throws a ConvergenceWarning and RF doesn't - no warning
# doesn't mean trustworthy, it just means training finished without
# numerical issues.

# --- Task 2: The right fix ---
scaled_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])
scaled_lr.fit(X_train, y_train)
prob_slr = scaled_lr.predict_proba(X_test)[:, 1]
brier_slr = brier_score_loss(y_test, prob_slr)

# Unscaled features made the solver stop at half-optimized coefficients,
# so the probabilities computed from those coefficients were also
# half-optimized - scaling let it fully converge, giving genuinely
# optimized (and more honest) probabilities.

# --- Task 3: The calibrator ---
calibrated_lr = CalibratedClassifierCV(estimator=scaled_lr, method='sigmoid', cv=5)
calibrated_lr.fit(X_train, y_train)
proba_cal_lr = calibrated_lr.predict_proba(X_test)[:, 1]
brier_cal_lr = brier_score_loss(y_test, proba_cal_lr)

calibrated_rf = CalibratedClassifierCV(estimator=modelrf, method='sigmoid', cv=5)
calibrated_rf.fit(X_train, y_train)
proba_cal_rf = calibrated_rf.predict_proba(X_test)[:, 1]
brier_cal_rf = brier_score_loss(y_test, proba_cal_rf)

print("Brier unscaled LR:      ", brier_lr)
print("Brier scaled LR:        ", brier_slr)
print("Brier calibrated LR:    ", brier_cal_lr)
print("Brier RF uncalibrated:  ", brier_rf)
print("Brier RF calibrated:    ", brier_cal_rf)

# cv=5 works the same way it did in StackingClassifier: it produces
# out-of-fold probabilities so the calibrator never learns from
# predictions the model made on data it already memorized.
# Calibration made both LR and RF worse here (not better) - the raw
# scaled LR was already reasonably honest, so the calibrator's
# corrections were mostly noise, not a real fix.

# --- Task 4: Reliability check ---
def reliability_bins(y_true, proba, n_bins=10):
    bins = np.linspace(0, 1, n_bins + 1)
    bin_ids = np.clip(np.digitize(proba, bins) - 1, 0, n_bins - 1)
    for i in range(n_bins):
        mask = bin_ids == i
        if mask.sum() == 0:
            continue
        print(f"Bin {i}: mean predicted={proba[mask].mean():.3f}, "
              f"actual fraction positive={y_true[mask].mean():.3f}, n={mask.sum()}")

print("\n--- Scaled LR (before calibration) ---")
reliability_bins(y_test, prob_slr)

print("\n--- Scaled LR (calibrated) ---")
reliability_bins(y_test, proba_cal_lr)


"""
My final verdict 
Calibration is not a must it is mostly used on model like SVM and model trained on large or heavily imbalanced dataset , where the probability are naturally dishonest
On this Dataset I'm deploying the raw uncalibrated model the logistics regression model in fact
Day 50 soft vote used probability score to weigh the vote but what happens when the probability is a lie ? That's where brier comes in it actually actually as the "lie checker" it punishes the lie alongside the calibrator

Day 50's soft voting lost because unscaled LR's probabilities were dishonest,so the real Day 50 fix was never "add a calibrator", it was "scale LR before letting it vote
And if LR was scaled and reran ,its probability estimates would likely be honest enough that soft voting might actually beat hard voting this time
"""