from sklearn.neighbors import KNeighborsClassifier

class KNearestNeighbor:
    def __init__(self):
        self.classifier = KNeighborsClassifier()

    def fit(self, x_train, y_train):
        return self.classifier.fit(x_train, y_train)

    def predict(self, x_train):
        return self.classifier.predict(x_train)

    def predict_proba(self, x_train):
        return self.classifier.predict_proba(x_train)

    def set_param(self, param):
        return self.classifier.set_params(**param)

    def score(self, x_train, y_train):
        return self.classifier.score(x_train, y_train)