import serial
import numpy as np
import pandas as pd
import time

NUM_SENSORS = 8


def main():
    ser = serial.Serial('COM29', 9600)
    output = [['Reading 1', 'Reading 2', 'Reading 3', 'Reading 4', 'Reading 5', 'Reading 6', 'Reading 7', 'Reading 8']]
    collect(ser, output)


def calibrate(ser):
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


def collect(ser, output):
    baseline = calibrate(ser)
    while ser.is_open:
        # AUTOCALIBRATE GOES HERE
        if False:
            calibrate(ser)

        try:
            row = np.array(ser.readline() \
                           .decode(). \
                           strip(). \
                           split(',')). \
                astype(int)
            if len(row) == NUM_SENSORS:
                # output.append(np.subtract(row, baseline))
                output.append(row)
        except:
            break
    ser.close()

    df = pd.DataFrame(output[1:], columns=output[0])
    df['Label'] = 'left leg cross'
    df['Baseline'] = ",".join(baseline.astype(str))
    # for i in range(1, 5):
        # df = df[df['Reading '+ str(i)] > baseline[i-1] + 50]
    df = df[300:]
    df.to_csv('../data/left_leg_cross_kevin.csv', index=False)

    return df


if __name__ == "__main__":
    main()
