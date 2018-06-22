#!/usr/bin/env python3

import matplotlib.pyplot as plt

from .reader import read_battery_history


def plot(df, canvas):
    canvas.plot(df.datetime, df.percent, label='Level', color='#ddddff')
    canvas.plot(df.datetime, df.percent_7_day_rolling,
                linewidth=1, label='7-day average')
    canvas.plot(df.datetime, df.percent_30_day_rolling,
                linewidth=1, label='30-day average')

    canvas.axhline(y=20, linewidth=1, color='r', alpha=0.5)
    canvas.axhline(y=44, linewidth=1, color='g', alpha=0.5)
    canvas.axhline(y=58, linewidth=1, color='g', alpha=0.5)
    canvas.axhline(y=80, linewidth=1, color='r', alpha=0.5)

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Date')
    canvas.set_ylabel('Battery level (%)')
    canvas.set_title('Battery history')


def main():
    fig, ax = plt.subplots()
    plot(df=read_battery_history(), canvas=ax)
    plt.show()


if __name__ == '__main__':
    main()
