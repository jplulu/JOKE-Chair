import joblib
from backend.classification_pipline import classify_posture, read_data
import os
import time
import pandas as pd



df = pd.read_csv('data/combined_data.csv')
# Get dictionary for categorical coding
c = df.Label.astype('category')
code_to_posture = dict(enumerate(c.cat.categories))
# Categorical coding
# df['Label'] = df['Label'].astype('category').cat.codes
# inv_map = {v: k for k, v in code_to_posture.items()}


# print(code_to_posture)
# exit(0)

CLASSIFIER_FILE = "classifier/logistic_regression_model.pkl"

classifier = joblib.load(CLASSIFIER_FILE)

prev_posture = ""
while True:
    posture_data = read_data()
    classification = classify_posture(classifier, posture_data)

    if prev_posture != classification:
        os.system('cls')
        print(code_to_posture[classification])
        prev_posture = classification