from collections import Counter
from math import log
from typing import List


class NaiveBayesClassifier:

    def __init__(self, X, y, alpha=0.05):
        self.alpha = alpha
        self.X = X  # learning values
        self.y = y

    def fit(self, X, y):  # X - titles array, y - labels array
        """ Fit Naive Bayes classifier according to X, y. """
        pos = 0
        act = 0
        for label in y:
            if label == 'good':
                pos += 1
            elif label == 'maybe':
                act += 1
        p_pos = pos / len(y)
        p_act = act / len(y)
        p_neg = 1 - p_pos - p_act

        counter_pos = Counter()
        counter_act = Counter()
        counter_neg = Counter()
        all_words = Counter()
        for i in range(len(y)):
            X[i].lower()
            if y[i] == 'good':
                counter_pos.update(X[i].split(' '))
            elif y[i] == 'maybe':
                counter_act.update(X[i].split(' '))
            else:
                counter_neg.update(X[i].split(' '))
            all_words.update(X[i].split(' '))

        d = len(all_words)  # размер вектора признаков - количество разных слов
        n_pos = len(counter_pos)  # это вроде не надо
        n_act = len(counter_act)
        n_neg = len(counter_neg)

        # подсчёт вероятностей встречи слова в каждом классе:
        c_pos = dict()
        c_act = dict()
        c_neg = dict()

        for word in all_words:
            c_pos[word] = (counter_pos[word] + self.alpha) / (all_words[word] + self.alpha * d)
            c_act[word] = (counter_act[word] + self.alpha) / (all_words[word] + self.alpha * d)
            c_neg[word] = (counter_neg[word] + self.alpha) / (all_words[word] + self.alpha * d)

        response = []
        response.append(n_pos)
        response.append(n_act)
        response.append(n_neg)
        response.append(c_pos)
        response.append(c_act)
        response.append(c_neg)
        return response

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        classy = self.fit(self.X, self.y)  # придумать где взять x и y

        y = []
        for title in X:
            title.lower()
            log_pos = log(classy[0])
            log_act = log(classy[1])
            log_neg = log(classy[2])
            for word in title.split(' '):
                if word in classy[3]:
                    log_pos += log(classy[3][word])
                    log_act += log(classy[4][word])
                    log_neg += log(classy[5][word])
            if log_pos == max(log_pos, log_act, log_neg):
                y.append('good')
            elif log_act == max(log_act, log_neg):
                y.append('maybe')
            else:
                y.append('never')

        return y

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        counter = 0
        for i in range(len(X_test)):
            if self.predict(X_test)[i] == y_test[i]:
                counter += 1
        return counter/len(X_test)
