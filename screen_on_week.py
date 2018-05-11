#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

import reader
from common import smoothed_line


def plot(df, canvas):
    analyzer = reader.Analyzer(df)
    start = df['date'].min()
    end = df['date'].max()
    index = pd.date_range(start, end, freq='W')

    lol = []
    for date in index:
        val = analyzer.screen_on_percent_by_week(date=date)
        lol.append(val / 100 * 24)

    canvas.plot(index, lol)
    canvas.scatter(index, lol, alpha=0.2)
    canvas.axhline(y=4, linewidth=1, color='r', alpha=0.5)
    canvas.set_xlabel('Week')
    canvas.set_ylabel('Screen on time per day (hr)')
    canvas.set_title('Screen on by week')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    df = reader.read_battery_history()
    plot(df=df, canvas=ax)
    plt.show()