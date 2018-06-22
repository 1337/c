#!/usr/bin/env python3

import matplotlib.pyplot as plt

from .reader import get_last_30_days, get_last_7_days, read_battery_history


def plot(df, canvas, **options):
    values = df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(df) * 100)
        except KeyError:
            ys.append(0)
    canvas.plot(range(100), ys, label='Lifetime')

    last_30_df = get_last_30_days(df)
    values = last_30_df.percent.value_counts()
    ys = []
    for idx in range(100):
        try:
            ys.append(values[idx] / len(last_30_df) * 100)
        except KeyError:
            ys.append(0)
    canvas.plot(range(100), ys, label='Last 30 days')

    if options.get('render_7_days', False):
        last_7_df = get_last_7_days(df)
        values = last_7_df.percent.value_counts()
        ys = []
        for idx in range(100):
            try:
                ys.append(values[idx] / len(last_7_df) * 100)
            except KeyError:
                ys.append(0)
        canvas.plot(range(100), ys, label='Last 7 days')

    canvas.legend(loc="upper left")
    canvas.axvline(x=20, linewidth=1, color='r', alpha=0.5)
    canvas.axvline(x=80, linewidth=1, color='r', alpha=0.5)
    canvas.set_xlabel('Battery level (%)')
    canvas.set_ylabel('Proportion time spent in given battery level (%)')
    canvas.set_title('Battery level frequency')


def main():
    fig, ax = plt.subplots()
    plot(df=read_battery_history(), canvas=ax)
    plt.show()


if __name__ == '__main__':
    main()
