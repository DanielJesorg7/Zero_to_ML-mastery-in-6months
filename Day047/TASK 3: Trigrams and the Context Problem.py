from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pandas as pd   # not actually used
import numpy as np    # not actually used

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
# Trigrams, max_features=200
vectorizer_3 = TfidfVectorizer(ngram_range=(1, 3), max_features=200)
pipeline_3 = Pipeline([
    ('tfidf', vectorizer_3),
    ('model', LogisticRegression(random_state=42))
])
pipeline_3.fit(X_train, y_train)
y_pred_3 = pipeline_3.predict(X_test)
print("Trigram (200 features) Accuracy:", accuracy_score(y_test, y_pred_3))
print(pipeline_3.named_steps['tfidf'].get_feature_names_out())

# Trigrams, max_features=500
vectorizer_4 = TfidfVectorizer(ngram_range=(1, 3), max_features=500)
pipeline_4 = Pipeline([
    ('tfidf', vectorizer_4),
    ('model', LogisticRegression(random_state=42))
])
pipeline_4.fit(X_train, y_train)
y_pred_4 = pipeline_4.predict(X_test)
print("Trigram (500 features) Accuracy:", accuracy_score(y_test, y_pred_4))