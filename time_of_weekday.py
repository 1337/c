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
            .by_weekday_and_hour([0, 1, 2, 3, 4], hour) \
            .screen_on_percent
        day_plot.append((hour, val))
    plot_smooth_line(canvas=canvas, xys=day_plot, color='#99ccff',
                     label='Weekdays')

    day_plot = []
    for hour in range(24):
        val = reader.Analyzer(df) \
            .by_weekday_and_hour([5, 6], hour) \
            .screen_on_percent
        day_plot.append((hour, val))
    plot_smooth_line(canvas=canvas, xys=day_plot, color='#ff6600',
                     label='Weekends')

    # Africa stats
    # https://www.slideshare.net/merlien/clustering-by-mobile-usage-and-behaviour-the-many-faces-of-smartphone-users-in-south-africa-gfk
    normal_human_beings = [
        (0, 2 * 1.66),
        (1, 1.5 * 1.66),
        (2, 1 * 1.66),
        (3, 1 * 1.66),
        (4, 1 * 1.66),
        (5, 2 * 1.66),
        (6, 3 * 1.66),
        (7, 4 * 1.66),
        (8, 5.5 * 1.66),
        (9, 5.5 * 1.66),
        (10, 6 * 1.66),
        (11, 6 * 1.66),
        (12, 6 * 1.66),
        (13, 6 * 1.66),
        (14, 6 * 1.66),
        (15, 6.5 * 1.66),
        (16, 6.5 * 1.66),
        (17, 7 * 1.66),
        (18, 7.5 * 1.66),
        (19, 7.5 * 1.66),
        (20, 7.5 * 1.66),
        (21, 6 * 1.66),
        (22, 5 * 1.66),
        (23, 5 * 1.66),
    ]
    plot_smooth_line(canvas=canvas, xys=normal_human_beings,
                     color='#91150e',
                     label='Normal human beings')

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Time of day (h)')
    canvas.set_ylabel('Probability screen is on (%)')
    canvas.set_title('Screen on by weekday/weekend')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    df = reader.read_battery_history()
    plot(df=df, canvas=ax)
    plt.show()
