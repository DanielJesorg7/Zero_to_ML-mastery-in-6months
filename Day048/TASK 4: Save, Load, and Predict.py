from sklearn.model_selection import GridSearchCV
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

pipeline_tune = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('model', MultinomialNB())
])

param_grid = {
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'tfidf__max_features': [1000, 5000],
    'model__alpha': [0.1, 1.0, 10.0]
}

grid = GridSearchCV(pipeline_tune, param_grid, cv=StratifiedKFold(3, shuffle=True, random_state=42))
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)

best_model = grid.best_estimator_
test_accuracy = best_model.score(X_test, y_test)
print("Test accuracy:", test_accuracy)

import joblib

joblib.dump(best_model, "text_classifier.joblib")

loaded_model = joblib.load("text_classifier.joblib")

original_preds = best_model.predict(X_test)
loaded_preds = loaded_model.predict(X_test)

import numpy as np
print("Predictions match:", np.array_equal(original_preds, loaded_preds))


new_posts = [
    "The rocket launch was successful and reached orbit",
    "The hockey team scored three goals in overtime",
    "The government passed a new law about weapons"
]

predictions = loaded_model.predict(new_posts)
print(predictions)

for pred in predictions:
    print(data.target_names[pred])