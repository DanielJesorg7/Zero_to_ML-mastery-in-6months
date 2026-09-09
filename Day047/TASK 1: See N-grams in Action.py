from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = [
    "This product is not good",
    "This product is good",
    "Not bad at all",
    "Really not good",
    "Absolutely good"
]

# Unigrams only
vectorizer_1 = TfidfVectorizer(ngram_range=(1, 1))
X1 = vectorizer_1.fit_transform(corpus)          # what method combines fit + transform?

print(vectorizer_1.get_feature_names_out())
df1 = pd.DataFrame(X1.toarray(), columns=vectorizer_1.get_feature_names_out())
print(df1)

# Unigrams + bigrams
vectorizer_2 = TfidfVectorizer(ngram_range=(1, 2))
X2 = vectorizer_2.fit_transform(corpus)

print(vectorizer_2.get_feature_names_out())
df2 = pd.DataFrame(X2.toarray(), columns=vectorizer_2.get_feature_names_out())
print(df2)

"""
Not good doesn't appear in sentence 1
"""