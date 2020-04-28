from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

from bayes import NaiveBayesClassifier
import string
from database import session, News


def clean(s):
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)


s = session()

data = s.query(News).filter(News.label != None).all()
length = int(len(data) * 0.7)
X = [clean(new.title) for new in data]  # lower in in classifier
y = [new.label for new in data]

X_train, y_train, X_test, y_test = X[:length], y[:length], X[length:], y[length:]

model = NaiveBayesClassifier(X_train, y_train)
print(model.score(X_test, y_test))

other_model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB(alpha=0.05)),
])

other_model.fit(X_train, y_train)
print(other_model.score(X_test, y_test))
