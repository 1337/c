#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    canvas.plot(df.percent, linewidth=1)
    canvas.axhline(y=80, linewidth=1, color='r')
    canvas.axhline(y=58, linewidth=1, color='g')
    canvas.axhline(y=40, linewidth=1, color='g')


if __name__ == '__main__':
    plot(df=reader.read_battery_history(),
         canvas=plt)
    plt.show()
