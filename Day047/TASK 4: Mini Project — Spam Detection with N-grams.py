from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

texts = [
    "Win a free iPhone now click here","Congratulations you won a prize click now",
    "Free money available today only hurry","Click here to claim your reward now",
    "You have been selected for a free gift","Limited time offer buy now click here",
    "Get rich quick click here to learn more","You won a free vacation claim now",
    "Meeting rescheduled to 3pm tomorrow","Please review the attached report by Friday",
    "Lunch at noon with the team today","Project deadline is next Friday",
    "Can we schedule a call next week","The quarterly results are in the folder",
    "Reminder dentist appointment on Monday","Your package has been delivered today",
    "Thanks for your help yesterday","Team meeting moved to room 302",
    "Please submit your timesheet by Friday","The client meeting is at 2pm today"
]
labels = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

Xs_train, Xs_test, ys_train, ys_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

spam_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), stop_words='english')),
    ('model', MultinomialNB())
])
spam_pipeline.fit(Xs_train, ys_train)
ys_pred = spam_pipeline.predict(Xs_test)
print("Spam Accuracy:", accuracy_score(ys_test, ys_pred))
print(confusion_matrix(ys_test, ys_pred))

new_msgs = ["Free gift waiting for you click here now",
            "The meeting is rescheduled to 4pm",
            "You won a prize claim your free reward"]
print(spam_pipeline.predict(new_msgs))


# Why do bigrams help spam detection more than unigrams?
# Bigrams capture strong spam phrases that individual words miss.
# Example from the dataset: the bigram "click here" appears in multiple spam messages
# ("Win a free iPhone now click here", "Click here to claim your reward now", etc.).
# The single words "click" or "here" are much weaker signals on their own.