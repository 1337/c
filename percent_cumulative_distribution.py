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
    canvas.plot(ys)


    last_31_days_df = reader.get_last_31_days(df)
    last_31_values = last_31_days_df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            cum = sum(last_31_values.get(x, 0) for x in range(idx))
            ys.append(cum)
        except KeyError:
            ys.append(0)

    ys = [y/max(ys)*100 for y in ys]  # Normalize to 100
    canvas.plot(ys)

    canvas.axvline(x=20, linewidth=1, color='r')
    canvas.axvline(x=80, linewidth=1, color='r')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(),
         canvas=ax)

    ax.set_xlabel('Battery level (%)')
    ax.set_ylabel('Cumulative time spent (%)')
    ax.set_title('Time spent in battery percentage by frequency, cumulative')

    plt.show()
