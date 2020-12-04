import serial
import numpy as np
from joblib import load

NUM_SENSORS = 8

clf = load('classifier.joblib')
ser = serial.Serial('COM29', 9600)
ser.flushInput()


def read_data(baseline):
    posture_data = []
    while len(posture_data) != NUM_SENSORS:
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


def calibrate():
    data = []
    for i in range(0, 100):
        row = np.array(ser.readline() \
                       .decode(). \
                       strip(). \
                       split(',')). \
            astype(int)
        if len(row) == NUM_SENSORS:
            data.append(row)

    temp = data[3:]
    baseline = np.mean(temp, axis=0)
    print(baseline)
    return baseline


baseline = calibrate()

while True:
    # TODO: Auto-Calibration?
    # Sleep for some time to put delay between each read?
    posture_data = read_data(baseline)
    posture = classify_posture(posture_data)
    # Process posture (notification and storage)