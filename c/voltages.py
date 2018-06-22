#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from .reader import get_last_7_days, read_battery_history


def plot(df, canvas):
    df = df[df.voltage > 0]

    canvas.scatter(
        df.percent,
        df.Voltage,
        s=3,
        c='#cccccc',
        alpha=0.07,
        label='Lifetime')
    canvas.set_xlabel('Battery percent')
    canvas.set_ylabel('Voltage (V)')
    canvas.set_title('Battery voltage by capacity')

    mdf = get_last_7_days(df)
    canvas.scatter(
        mdf.percent,
        mdf.Voltage,
        s=3,
        c='green',
        alpha=0.2,
        label='Last 7 days')

    # Polynomial trend line
    z = np.polyfit(df.percent, df.Voltage, deg=3)
    p = np.poly1d(z)
    points = sorted(df.percent)
    canvas.plot(points, p(points), c='#3bba9c')

    canvas.axhline(y=3.92, linewidth=1, color='r', alpha=0.5)
    canvas.legend(loc="upper left")


def main():
    fig, ax = plt.subplots()
    plot(df=read_battery_history(), canvas=ax)
    plt.show()


if __name__ == '__main__':
    main()
