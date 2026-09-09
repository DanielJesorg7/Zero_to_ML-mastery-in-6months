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

pipeline_1 = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,1))) ,
    ('model', LogisticRegression(random_state=42))
])

pipeline_1.fit(X_train, y_train)

pipeline_2 = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2))) ,
    ('model', LogisticRegression(random_state=42))
])

pipeline_2.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix

y_pred_1 = pipeline_1.predict(X_test)
print("Unigram Accuracy:", accuracy_score(y_test, y_pred_1))
print("Unigram Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_1))

y_pred_2 = pipeline_2.predict(X_test)
print("Bigram Accuracy:", accuracy_score(y_test, y_pred_2))
print("Bigram Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_2))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_2))

words_1 = pipeline_1.named_steps['tfidf'].get_feature_names_out()
coefs_1 = pipeline_1.named_steps['model'].coef_[0]
importance_df_1 = pd.DataFrame({'word': words_1, 'coef': coefs_1})

words_2 = pipeline_2.named_steps['tfidf'].get_feature_names_out()
coefs_2 = pipeline_2.named_steps['model'].coef_[0]
importance_df_2 = pd.DataFrame({'word': words_2, 'coef': coefs_2})


top_5_positive = importance_df_2.sort_values('coef', ascending=False).head(5)
top_5_negative = importance_df_2.sort_values('coef', ascending=True).head(5)
print("Top 5 positive bigrams:\n", top_5_positive)
print("Top 5 negative bigrams:\n", top_5_negative)

pred_1 = pipeline_2.predict(["This is the worst product I have ever bought"])
pred_2 = pipeline_2.predict(["Absolutely fantastic I love everything about it"])

"""
No — both pipelines scored identically at 0.8
"""