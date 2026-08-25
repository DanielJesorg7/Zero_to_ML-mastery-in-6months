import numpy as np
import pandas as pd

np.random.seed(42)
n = 300

age = np.random.randint(18, 70, n)
income = np.random.randint(100000, 2000000, n)
purchase_freq = np.random.randint(1, 50, n)
website_time = np.random.randint(1, 120, n)
support_tickets = np.random.randint(0, 10, n)

# email_opens correlated with purchase_freq
email_opens = purchase_freq + np.random.randint(-3, 3, n)

df = pd.DataFrame({
    "age": age,
    "income": income,
    "purchase_freq": purchase_freq,
    "website_time": website_time,
    "email_opens": email_opens,
    "support_tickets": support_tickets
})

df["churn"] = np.where(
    (df["support_tickets"] > 5) & (df["purchase_freq"] < 15) & (df["website_time"] < 30),
    1, 0
)
print(df.head())
print(df["churn"].value_counts())

X = df.drop("churn", axis=1)
y = df["churn"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pca = PCA(n_components=3)
pca.fit(X_train_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total info kept:", sum(pca.explained_variance_ratio_))

X_train_pca = pca.transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train_pca, y_train)
predictions = model.predict(X_test_pca)

print("Accuracy:", accuracy_score(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

new_customer = [[35, 600000, 5, 10, 4, 8]]

new_customer_scaled = scaler.transform(new_customer)
new_customer_pca = pca.transform(new_customer_scaled)

proba = model.predict_proba(new_customer_pca)
print("Churn probability [P(stay), P(churn)]:", proba)