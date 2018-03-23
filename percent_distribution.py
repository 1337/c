#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    values = df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(df))
        except KeyError:
            ys.append(0)

    canvas.plot(range(100), ys)

    last_31_df = reader.get_last_31_days(df)
    values = last_31_df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(last_31_df))
        except KeyError:
            ys.append(0)

    canvas.plot(range(100), ys)


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(),
         canvas=ax)

    plt.show()
