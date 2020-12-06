from sklearn.neighbors import KNeighborsRegressor

class KNearestNeighbor:
    def __init__(self):
        self.classifier = KNeighborsRegressor()

    def fit(self, x_train, y_train):
        return self.classifier.fit(x_train, y_train)

    def predict(self, x_train):
        return self.classifier.predict(x_train)

    def set_param(self, param):
        return self.classifier.set_params(**param)

    def score(self, x_train, y_train):
        return self.classifier.score(x_train, y_train)