import serial
import numpy as np
import pandas as pd
import time
NUM_SENSORS = 2

def main():
    ser = serial.Serial('COM3', 9600)
    output = [['Reading 1', 'Reading 2']]
    collect(ser, output)


def calibrate(ser):
    data = []
    for i in range(0,100):
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
            row = np.array(ser.readline()\
                              .decode().\
                              strip().\
                              split(',')).\
                              astype(int)
            if len(row) == NUM_SENSORS:
                output.append(np.subtract(row, baseline))
        except:
            break
    ser.close()

    df = pd.DataFrame(output[100:], columns=output[0])
    df.to_csv('test.csv', index=False)

    return df


if __name__ == "__main__":
    main()