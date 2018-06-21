import datetime

import numpy as np
from scipy.interpolate import spline


def str_to_date(x):
    if isinstance(x, datetime.date):
        return x
    return datetime.datetime.strptime(x, '%Y-%m-%d').date()


def date_time_to_datetime(x):
    date, hours_raw = x
    hours = int(hours_raw)
    seconds = (hours_raw - hours) * 100 * 60  # 0.3 in this case means 30 minutes
    time_in_hours = datetime.timedelta(hours=hours, seconds=seconds)
    return datetime.datetime.combine(
        date, datetime.datetime.min.time()) + time_in_hours


def clean_voltage(x):
    try:
        x = int(x)
    except (ValueError, TypeError):
        return 0
    if 0 <= x <= 4500000:
        return x
    return 0


def rounded(num):
    return round(num, 2)


def smoothed_x(xs, points=100):
    x_sm = np.array(xs)

    return np.linspace(x_sm.min(), x_sm.max(), points)


def smoothed_y(xs, ys, points):
    x_smooth = smoothed_x(xs, points=points)
    return spline(xs, ys, x_smooth)


def smoothed_line(*, points, data=None, xs=None, ys=None):
    # https://stackoverflow.com/a/25826265/1558430
    xs = xs or [x[0] for x in data]
    ys = ys or [x[1] for x in data]

    x_smooth = smoothed_x(xs, points=points)
    y_smooth = smoothed_y(xs, ys, points=points)

    return x_smooth, y_smooth
