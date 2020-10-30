from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


class LogisticRegressionClassifier:
    def __init__(self, penalty='l2', max_iter=100, solver='lbfgs'):
        self.clf = LogisticRegression(penalty=penalty, max_iter=max_iter, solver=solver, multi_class='multinomial')

    def fit(self, x_train, y_train):
        self.clf.fit(x_train, y_train)

    def predict(self, x_test):
        predictions = self.clf.predict(x_test)
        return predictions

    def score(self, x_test, y_test):
        predictions = self.predict(x_test)
        return (predictions == y_test).sum().astype(np.float64) / len(y_test)


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, header=None, names=[
    "Sepal length (cm)",
    "Sepal width (cm)",
    "Petal length (cm)",
    "Petal width (cm)",
    "Species"
])
df['Species'] = df['Species'].astype('category').cat.codes

np.random.seed(653)
df_shuffle = df.sample(frac=1)
df_x = df_shuffle.drop(['Species'], axis=1).values
df_y = df_shuffle['Species'].values

# Standardizing predictors to zero mean unit variance
df_x = (df_x - df_x.mean()) / df_x.std()

# Separate training, validation, and testing data
x_train, x_test = np.split(df_x, [int(0.8 * len(df_x))])
y_train, y_test = np.split(df_y, [int(0.8 * len(df_y))])

clf = LogisticRegressionClassifier()
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
