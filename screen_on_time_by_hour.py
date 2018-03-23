#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader
from common import smoothed_line

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


def plot(df, canvas):
    for day in range(7):
        day_plot = []
        stats_on_day = df[df.weekday == day]
        for hour in range(24):
            hour_points = stats_on_day[
                (stats_on_day.hour >= hour) &
                (stats_on_day.hour < hour + 1)]
            hour_on = hour_points[hour_points.display == 'on']
            hour_off = hour_points[hour_points.display == 'off']

            val = max(
                hour_on.count() /
                (hour_on.count() + hour_off.count())) * 100
            day_plot.append((hour, val))

        x_smooth, y_smooth = smoothed_line(data=day_plot, points=points)

        if day == 0:
            canvas.plot(x_smooth, y_smooth, color=colors[day],
                        label='Weekdays')
        elif day == 6:
            canvas.plot(x_smooth, y_smooth, color=colors[day],
                        label='Weekends')
        else:
            canvas.plot(x_smooth, y_smooth, color=colors[day])

    canvas.legend(loc='upper left')
    canvas.set_xlabel('Time of day (h)')
    canvas.set_ylabel('Probability screen is on (%)')
    canvas.set_title('Screen usage by day of week and time of day')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
