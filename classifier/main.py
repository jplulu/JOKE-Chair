import sklearn
from sklearn.neighbors import KNeighborsRegressor
from sklearn import datasets
from sklearn.model_selection import train_test_split


class KNearestNeighbor:
    def __init__(self):
        self.classifier = KNeighborsRegressor()

    def fit(self, X, Y):
        return self.classifier.fit(X, Y)

    def predict(self, X):
        return self.classifier.predict(X)

    def set_param(self, param):
        return self.classifier.set_params(**param)

    def score(self, X, y):
        return self.classifier.score(X, y)


if __name__ == '__main__':
    test = KNearestNeighbor()
    param = {"n_neighbors":5, "weights":'uniform', 'algorithm':'auto',
             'leaf_size':30,"p":2 , "metric":"minkowski", "metric_params":None,
            "n_jobs":None}
    test.set_param(param)

    iris = datasets.load_iris()

    X = iris.data
    y = iris.target
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)
    test.fit(x_train, y_train)

    prediction = test.predict(x_test)
    score = test.score(x_test, y_test)
    print(score)
