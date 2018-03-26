#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    canvas.scatter(df.index, df.percent, label='Level', color='#ddddff', marker='x')
    canvas.plot(df.percent_7_day_rolling, linewidth=1, label='7-day average')
    canvas.plot(df.percent_30_day_rolling, linewidth=1, label='30-day average')

    canvas.axhline(y=20, linewidth=1, color='r')
    canvas.axhline(y=44, linewidth=1, color='g')
    canvas.axhline(y=58, linewidth=1, color='g')
    canvas.axhline(y=80, linewidth=1, color='r')

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Entry index')
    canvas.set_ylabel('Battery level (%)')
    canvas.set_title('Battery history')


if __name__ == '__main__':
    fig, ax = plt.subplots()

    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
