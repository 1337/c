#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader
from common import smoothed_line


def plot_smooth_line(canvas, xys, points=480, color=None, label=None):
    x_smooth, y_smooth = smoothed_line(data=xys, points=points)
    kwargs = {}
    if color:
        kwargs['color'] = color
    if label:
        kwargs['label'] = label
    canvas.plot(x_smooth, y_smooth, **kwargs)


def plot(df, canvas):
    plot = []
    for hour in range(24):
        val = reader.Analyzer(df) \
            .by_weekday_and_hour(hour=hour) \
            .screen_on_percent
        plot.append((hour, val))

    plot_smooth_line(canvas=canvas,
                     xys=plot,
                     color='#b5b5b5',
                     label='Lifetime')

    last_30_days_df = reader.get_last_30_days(df)
    last_30_plot = []
    for hour in range(24):
        val = reader.Analyzer(last_30_days_df) \
            .by_weekday_and_hour(hour=hour) \
            .screen_on_percent
        last_30_plot.append((hour, val))

    plot_smooth_line(canvas=canvas,
                     xys=last_30_plot,
                     color='#2ca82a',
                     label='Last 30 days')

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Time of day (h)')
    canvas.set_ylabel('Probability screen is on (%)')
    canvas.set_title('Screen on by time of day')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    df = reader.read_battery_history()
    plot(df=df, canvas=ax)
    plt.show()
