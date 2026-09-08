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

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)
print("Shape:", X.shape)

print("__________________________")
print(df["learning"])


"""23 unique words in vocabulary. "Learning" appears in 5 of the 6 sentences (all except sentence 4 — "Python is easy to learn and use," which uses "learn" not "learning," a different word to the vectorizer since it doesn't stem words by default).
"""