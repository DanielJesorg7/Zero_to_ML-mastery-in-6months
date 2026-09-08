from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

corpus = [
    "Machine learning is amazing and powerful",
    "Python is great for machine learning",
    "I love learning new things every day",
    "Machine learning and deep learning are related",
    "Python is easy to learn and use",
    "Deep learning is a subset of machine learning"
]

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer1 = TfidfVectorizer(stop_words='english')
X1 = vectorizer1.fit_transform(corpus)

vectorizer2 = CountVectorizer()
X2 = vectorizer2.fit_transform(corpus)

print(vectorizer1.get_feature_names_out())
df_tfidf = pd.DataFrame(X1.toarray(), columns=vectorizer1.get_feature_names_out()).round(3)
print(df_tfidf.round(3))

print(vectorizer2.get_feature_names_out())
df_count = pd.DataFrame(X2.toarray(), columns=vectorizer2.get_feature_names_out())
print(df_count)

print("___________________-----___+_-_---")
print(df_tfidf.loc[0].sort_values(ascending=False))

"""
yes, "amazing" scores higher than "learning," and here's why: "learning" appears in 5 of your 6 sentences, so IDF (Inverse Document Frequency) heavily penalizes it — it's treated almost like a filler word because it's so common across your corpus, even though it wasn't stripped as a stop word. "Amazing" appears in only 1 sentence, so it gets zero penalty — IDF boosts it as a rare, distinguishing word.
"""