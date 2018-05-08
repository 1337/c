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

    normal_human_beings = [
        (0, 3),
        (1, 2),
        (2, 1.5),
        (3, 1),
        (4, 1.5),
        (5, 2),
        (6, 5),
        (7, 5),
        (8, 9),
        (9, 15),
        (10, 4),
        (11, 3),
        (12, 3),
        (13, 4),
        (14, 3),
        (15, 3),
        (16, 3),
        (17, 4),
        (18, 5),
        (19, 5),
        (20, 4),
        (21, 6),
        (22, 6),
        (23, 5),
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
