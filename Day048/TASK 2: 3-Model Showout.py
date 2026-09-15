from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.datasets import fetch_20newsgroups

categories = ['sci.space', 'rec.sport.hockey', 'talk.politics.guns']
data = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'), random_state=42)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline_nb = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1,1))),
    ('model', MultinomialNB())
])

pipeline_lr = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1,1))),
    ('model', LogisticRegression(max_iter=1000, random_state=42))
])

pipeline_rf = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1,1))),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

scores_nb = cross_val_score(pipeline_nb, X_train, y_train, cv=skf)
scores_lr = cross_val_score(pipeline_lr, X_train, y_train, cv=skf)
scores_rf = cross_val_score(pipeline_rf, X_train, y_train, cv=skf)

print("Naive Bayes mean accuracy:", scores_nb.mean())
print("Logistic Regression mean accuracy:", scores_lr.mean())
print("Random Forest mean accuracy:", scores_rf.mean())

"""
Naive Bayes wins, but the gap between NB and LR is small — not hugely significant
"""
