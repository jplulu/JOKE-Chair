import joblib
import pandas as pd
import numpy as np
import random

# df = pd.read_csv('../data/varied_data.csv')
df = pd.read_csv('../data/combined_data.csv')
# Get dictionary for categorical coding
# c = df.Label.astype('category')
# code_to_posture = dict(enumerate(c.cat.categories))
# # Categorical coding
# df['Label'] = df['Label'].astype('category').cat.codes

for i in range(len(df)):
    for j in range(1, 9):
        df.loc[i, 'Reading {}'.format(j)] = df.loc[i, 'Reading {}'.format(j)] - random.randrange(-60, 60)
df.to_csv("../data/varied_data.csv", index=False)

print(df.head)
np.random.seed(4321)
df_shuffle = df.sample(frac=1).drop(['Baseline'], axis=1)
df_x = df_shuffle.drop(['Label'], axis=1).values
df_y = df_shuffle['Label'].values
df_x = (df_x - df_x.mean()) / df_x.std()
CLASSIFIER_FILE = "./logistic_regression_model.pkl"

clf = joblib.load(CLASSIFIER_FILE)
predictions = clf.predict(df_x)
score = (predictions == df_y).sum().astype(np.float64) / len(df_y)
print(score)
