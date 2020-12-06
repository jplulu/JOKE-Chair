from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


class RandomForest:

    def __init__(self, params=None, x_train=None, y_train=None):
        if params == None:
            self.classifier = RandomForestClassifier()
        else:
            self.classifier = RandomForestClassifier(**params)
        self.predictions = []
        self.x_train = x_train
        self.y_train = y_train
        if x_train is not None and y_train is not None:
            self.fit(self.x_train, self.y_train)

    def fit(self, x_train, y_train, sample_weight=None):
        self.classifier.fit(x_train, y_train, sample_weight=sample_weight)
        return self

    def predict(self, X):
        self.predictions = self.classifier.predict(X)
        return self.predictions

    def get_parameters(self):
        self.predictions = self.classifier.get_params()
        return self.classifier.get_params()

    def set_parameters(self, params):
        self.classifier.set_params(**params)
        return self

    def score(self, X, y, sample_weight=None):
        return self.classifier.score(X, y, sample_weight=sample_weight)

    def predict_probability(self, X):
        return self.classifier.predict_proba(X)

    def set_data(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        return self

    def confusion_matrix(self, y_true):
        return confusion_matrix(y_true, self.predictions)


