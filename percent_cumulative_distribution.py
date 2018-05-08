#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    values = df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            cum = sum(values.get(x, 0) for x in range(idx))
            ys.append(cum)
        except KeyError:
            ys.append(0)

    ys = [y/max(ys)*100 for y in ys]  # Normalize to 100
    canvas.plot(ys, label='Lifetime')

    last_30_days_df = reader.get_last_30_days(df)
    last_30_values = last_30_days_df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            cum = sum(last_30_values.get(x, 0) for x in range(idx))
            ys.append(cum)
        except KeyError:
            ys.append(0)

    ys = [y/max(ys)*100 for y in ys]  # Normalize to 100
    canvas.plot(ys, label='Last 30 days')

    canvas.legend(loc="upper left")
    canvas.axvline(x=20, linewidth=1, color='r', alpha=0.5)
    # canvas.axvline(x=44, linewidth=1, color='g')
    # canvas.axvline(x=58, linewidth=1, color='g')
    canvas.axvline(x=80, linewidth=1, color='r', alpha=0.5)
    canvas.set_xlabel('Battery level (%)')
    canvas.set_ylabel('Cumulative time spent (%)')
    canvas.set_title('Battery percentage cumulative frequency')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
