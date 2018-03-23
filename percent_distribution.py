#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    values = df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(df) * 100)
        except KeyError:
            ys.append(0)

    canvas.plot(range(100), ys, label='Lifetime')

    last_30_df = reader.get_last_30_days(df)
    values = last_30_df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(last_30_df) * 100)
        except KeyError:
            ys.append(0)

    canvas.plot(range(100), ys, label='Last 30 days')

    canvas.legend(loc="upper left")
    canvas.axvline(x=20, linewidth=1, color='r')
    # canvas.axvline(x=44, linewidth=1, color='g')
    # canvas.axvline(x=58, linewidth=1, color='g')
    canvas.axvline(x=80, linewidth=1, color='r')
    canvas.set_xlabel('Battery level (%)')
    canvas.set_ylabel('Proportion time spent in given battery level (%)')
    canvas.set_title('Battery level frequency')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
