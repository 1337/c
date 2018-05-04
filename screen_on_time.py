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
    day_plot = []
    for hour in range(24):
        val = reader.Analyzer(df) \
            .by_day_and_hour([0, 1, 2, 3, 4], hour) \
            .screen_on_percent
        day_plot.append((hour, val))
    plot_smooth_line(canvas=canvas, xys=day_plot, color='#99ccff',
                     label='Weekdays')

    day_plot = []
    for hour in range(24):
        val = reader.Analyzer(df) \
            .by_day_and_hour([5, 6], hour) \
            .screen_on_percent
        day_plot.append((hour, val))
    plot_smooth_line(canvas=canvas, xys=day_plot, color='#ff6600',
                     label='Weekends')

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Time of day (h)')
    canvas.set_ylabel('Probability screen is on (%)')
    canvas.set_title('Screen on by day of week and time of day')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    df = reader.read_battery_history()
    plot(df=df, canvas=ax)
    plt.show()
