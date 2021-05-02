import pandas as pd
import numpy as np
from classifier.logistic_regression import LogisticRegressionClassifier
from classifier.random_forest import RandomForest
from classifier.knearestneighbor import KNearestNeighbor
import joblib
from sklearn2pmml import sklearn2pmml
from sklearn_pandas import DataFrameMapper


df = pd.read_csv('data/combined_data.csv')
cols = ["Reading " + str(i) for i in range(1, 11)]
cols.append("Label")
df = df[cols]

proper = df[df['Label'] == 'proper'].reset_index(drop=True)
del proper['Label']
baseline = proper.mean()
for i in range(1, 11):
    df['Reading ' + str(i)] = df['Reading ' + str(i)] - baseline[i-1]


clf = LogisticRegressionClassifier()

seed = np.random.randint(10000)

c = df.Label.astype('category')
code_to_posture = dict(enumerate(c.cat.categories))
# Categorical coding
df['Label'] = df['Label'].astype('category').cat.codes

# 1: Back Top Right
# 2: Back Bottom Left
# 3: Back Top Left
# 4: Back Bottom Right
# 5: Front Left
# 6: Mid Left
# 7: Back left
# 8: Front Right
# 9: Mid Right
# 10: Back Right

# Shuffle and divide feature and label
np.random.seed(seed)
df_shuffle = df.sample(frac=1)
df_x = df_shuffle.drop(['Label'], axis=1).values
df_y = df_shuffle['Label'].values
# Standardizing predictors to zero mean unit variance
df_x = (df_x - df_x.mean()) / df_x.std()

# Separate training, validation, and testing data
x_train, x_test = np.split(df_x, [int(0.8 * len(df_x))])
y_train, y_test = np.split(df_y, [int(0.8 * len(df_y))])

clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)
prob = clf.clf.predict_proba(x_test).tolist()



# Converting coding back to posture
predicted_postures = []
for (i, y) in zip(range(0,len(prob)), y_predict):
    predicted_postures.append(code_to_posture[y])
    prob[i].append(code_to_posture[y])

test = pd.DataFrame(prob)

test.to_csv('prob.csv', index=False)

score = clf.score(x_test, y_test)

output = []

header = ["Reading " + str(i) for i in range(1, 11)]
header.insert(0, "Label")

output.append(header)

for label in df['Label'].unique():
    temp = df[df['Label'] == label]
    del temp['Label']

    print(code_to_posture[label])

    row = temp.mean().tolist()
    row.insert(0, code_to_posture[label])
    output.append(row)

outdf = pd.DataFrame(output[1:], columns=output[0])

outdf.to_csv('test.csv', index=False)