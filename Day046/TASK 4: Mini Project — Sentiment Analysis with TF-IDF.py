from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

reviews = [
    "This product is amazing and works perfectly",
    "Terrible quality broke after one day",
    "Absolutely love it best purchase ever",
    "Waste of money do not buy this",
    "Great value for the price highly recommend",
    "Stopped working within a week very disappointed",
    "Exceeded my expectations fantastic product",
    "Cheap material fell apart immediately",
    "So happy with this purchase five stars",
    "Complete garbage worst product I have used",
    "Works as described no complaints",
    "Horrible customer service and defective item",
    "Love the design and functionality",
    "Not worth the price very poor quality",
    "Best product in this category hands down",
    "Arrived damaged and unusable",
    "Perfect for my needs would buy again",
    "Total scam do not trust this seller",
    "Reliable and durable great performance",
    "Very unhappy with the quality returning it"
]
sentiments = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1=positive, 0=negative


X_train, X_test, y_train, y_test = train_test_split(reviews, sentiments, test_size=0.25, random_state=42)

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=100)) ,
    ('model', LogisticRegression(random_state=42))
])

pipeline.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix

y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

words = pipeline.named_steps['tfidf'].get_feature_names_out()
coefs = pipeline.named_steps['model'].coef_[0]

importance_df = pd.DataFrame({'word': words, 'coef': coefs})
top_10 = importance_df.sort_values('coef', ascending=False).head(10)
print(top_10)

pred_1 = pipeline.predict([ "This is the worst product I have ever bought" ])
pred_2 = pipeline.predict([ "Absolutely fantastic I love everything about it" ])

print(pred_1)
print(pred_2)

"""
TF-IDF beats raw word counts here because it downweights common filler words and upweights rare, distinguishing words — meaning words like "garbage" or "amazing" (which show up in only one or two reviews) get more influence than words like "product" that show up everywhere and carry no sentiment signal on their own.
"""