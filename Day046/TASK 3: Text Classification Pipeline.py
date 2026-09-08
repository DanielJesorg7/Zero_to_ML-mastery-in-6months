from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


texts = [
    "Win a free iPhone now click here", "Congratulations you won a prize", 
    "Free money available today only", "Click here to claim your reward",
    "You have been selected for a free gift", "Limited time offer buy now",
    "Meeting rescheduled to 3pm tomorrow", "Please review the attached report",
    "Lunch at noon with the team", "Project deadline is next Friday",
    "Can we schedule a call next week", "The quarterly results are in",
    "Reminder: dentist appointment Monday", "Your package has been delivered",
    "Thanks for your help yesterday"
]
labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1=spam, 0=ham

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')) ,
    ('model', MultinomialNB())
])

pipeline.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


pred_1 = pipeline.predict(["Meeting moved to conference room B"])
pred_2 = pipeline.predict(["Free gift waiting for you click now"])

print(pred_1)
print(pred_2)