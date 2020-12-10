from sklearn.linear_model import LogisticRegression
import numpy as np


class LogisticRegressionClassifier:
    def __init__(self, penalty='l2', max_iter=500, solver='lbfgs'):
        self.clf = LogisticRegression(penalty=penalty, max_iter=max_iter, solver=solver, multi_class='multinomial')

    def fit(self, x_train, y_train):
        self.clf.fit(x_train, y_train)

    def predict(self, x_test):
        predictions = self.clf.predict(x_test)
        return predictions

    def score(self, x_test, y_test):
        predictions = self.predict(x_test)
        return (predictions == y_test).sum().astype(np.float64) / len(y_test)



