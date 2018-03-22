#!/usr/bin/env python3

import matplotlib.pyplot as plt

from common import smoothed_line
import reader

df = reader.read_battery_history()


colors = [
    '#6699ff',
    '#6699ff',
    '#6699ff',
    '#6699ff',
    '#6699ff',
    '#ff6600',
    '#ff6600',
]

points = 480

for day in range(7):
    day_plot = []
    stats_on_day = df[df.weekday == day]
    for hour in range(24):
        hour_points = stats_on_day[(stats_on_day.hour >= hour) & (stats_on_day.hour < hour + 1)]
        hour_on = hour_points[hour_points.display == 'on']
        hour_off = hour_points[hour_points.display == 'off']

        val = max(hour_on.count() / (hour_on.count() + hour_off.count()))
        day_plot.append((hour, val))

    x_smooth, y_smooth = smoothed_line(data=day_plot, points=points)

    plt.plot(x_smooth,
             y_smooth,
             color=colors[day])

plt.show()
