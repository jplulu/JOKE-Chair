import pandas as pd
import sys

POSTURES = ["proper", "lean forward", "lean right", "lean left", "slouch", "right leg cross", "left leg cross"]


def generate_data_set(filename):
    data_set = pd.DataFrame()
    for posture in POSTURES:
        df = pd.read_csv("{}.csv".format(posture))
        data_set = pd.concat([data_set, df]).reset_index(drop=True)

    data_set.to_csv("{}.csv".format(filename), index=False)

    exit(0)



if __name__ == "__main__":
    generate_data_set(sys.argv[1])