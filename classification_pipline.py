import serial
import numpy as np
from joblib import load

clf = load('classifier.joblib')
ser = serial.Serial('COM29', 9600)
ser.flushInput()


def read_data():
    ser.flushInput()
    posture_data = np.array(ser.readline() \
                            .decode(). \
                            strip(). \
                            split(',')). \
        astype(int)

    return posture_data


def classify_posture(posture_data):
    prediction = clf.predict(posture_data)
    return prediction


while True:
    # TODO: Calibration
    # Sleep for some time to put delay between each read?
    posture_data = read_data()
    posture = classify_posture(posture_data)
    # Process posture
