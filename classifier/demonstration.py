import joblib
from classification_pipline import classify_posture, read_data
import os

CLASSIFIER_FILE = ""

classifier = joblib.load(CLASSIFIER_FILE)

prev_posture = ""
while True:
    posture_data = read_data()
    classification = classify_posture(classifier, posture_data)

    if prev_posture != classification:
        os.system('cls')
        print(classification)
        prev_posture = classification