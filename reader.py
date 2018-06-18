# coding=utf-8

import glob
from datetime import timedelta

import arrow
import pandas as pd

from common import clean_voltage, rounded, str_to_date, date_time_to_datetime
from utils import time_tracker


def read_battery_history():
    """Add some processing"""
    input_files = glob.glob('*.csv')
    list_ = []
    for file_ in input_files:
        df = pd.read_csv(
            file_,
            delimiter=',',
            header=None,  # "csv has no headers"
            names=['date', 'hour', 'percent', 'display', 'voltage'])
        list_.append(df)
    df = pd.concat(list_)

    # Map function to column, then put the column back (or another column)
    with time_tracker('processing lol'):
        df['date'] = df['date'].apply(str_to_date)
        df['weekday'] = df['date'].apply(lambda x: x.isoweekday() - 1)
        df['hour'] = df['hour'].apply(float)
        df['percent'] = df['percent'].apply(int)
        df['voltage'] = df['voltage'].apply(clean_voltage)
        df['Voltage'] = df['voltage'].apply(lambda x: x / 1000000)

    with time_tracker('processing more lol'):
        # Do some maths
        df['datetime'] = df[['date', 'hour']].apply(date_time_to_datetime, axis=1)
        df['percent_row_before'] = df['percent'].shift(1)
        df['percent_row_after'] = df['percent'].shift(-1)
        df['percent_7_day_rolling'] = df['percent'].rolling(window=144 * 7).mean()
        df['percent_30_day_rolling'] = df['percent'].rolling(window=144 * 30).mean()

    return df


def get_last_n_days(*, df, n):
    n_days_ago = arrow.now().replace(days=-n).datetime
    return df[df.datetime > n_days_ago]


def get_last_30_days(df):
    return get_last_n_days(df=df, n=30)


def get_last_7_days(df):
    return get_last_n_days(df=df, n=7)


def get_between_20_80_times(df) -> int:
    return len(df[
        (20 <= df.percent) & (df.percent <= 80)])  # Conditions cannot be chained


def get_between_44_58_times(df) -> int:
    return len(df[
        (44 <= df.percent) &
        (df.percent <= 58)])  # Conditions cannot be chained


def get_charge_events(df) -> int:
    return len(df[
        (df.percent_row_before < df.percent) &
        (df.percent_row_after <= df.percent)])  # Inflection point


def get_discharge_events(df) -> int:
    return len(df[
        (df.percent_row_before > df.percent) &
        (df.percent_row_after > df.percent)])  # Not >= because 100% stays 100%


def get_charging_to_100_times(df) -> int:
    return len(df[
        (df.percent_row_before == df.percent) &
        (df.percent_row_after < df.percent) &
        (df.percent == 100)])


def get_charging_to_90_times(df) -> int:
    return len(df[
        (df.percent_row_before < 90) &
        (df.percent >= 90)])


def get_charging_to_80_times(df) -> int:
    return len(df[
        (df.percent_row_before < 80) &
        (df.percent >= 80)])


class Analyzer(object):
    df = None

    def __init__(self, df):
        self.df = df

    @property
    def days(self):
        return (self.df['date'].max() - self.df['date'].min()).days

    @property
    def between_20_80_times(self):
        return get_between_20_80_times(self.df)

    @property
    def between_44_58_times(self):
        return get_between_44_58_times(self.df)

    @property
    def between_20_80_percent(self):
        return rounded(self.between_20_80_times / len(self.df) * 100)

    @property
    def between_44_58_percent(self):
        return rounded(self.between_44_58_times / len(self.df) * 100)

    @property
    def charge_events(self):
        return get_charge_events(self.df)

    @property
    def discharge_events(self):
        return get_discharge_events(self.df)

    @property
    def charging_to_100_times(self):
        return get_charging_to_100_times(self.df)

    @property
    def charging_to_90_times(self):
        return get_charging_to_90_times(self.df)

    @property
    def charging_to_80_times(self):
        return get_charging_to_80_times(self.df)

    @property
    def average_voltage(self):
        return rounded(
            int(self.df[self.df.voltage > 0].voltage.mean()) / 1000000)

    @property
    def screen_on_percent(self):
        screen_on_df = self.df[self.df.display == 'on']
        return rounded(len(screen_on_df) / len(self.df) * 100)

    def screen_on_percent_by_weekday(self, weekday):
        day_df = self.df[self.df.weekday == weekday]

        # At a 10-minute collection interval, the number of points
        # collected per day is 144.
        # If we don't have 144 then obviously something's missing
        datapoints = 0 # 86400 / 600
        datapoints = max(datapoints, len(day_df))

        base_diff = datapoints - len(day_df)
        num_on = len(day_df[day_df.display == 'on'])

        frac = (base_diff + num_on) / datapoints
        return rounded(frac * 100)

    def screen_on_percent_by_week(self, date):
        dt = timedelta(days=1)
        week_df = self.df[
            (self.df.date >= date.date() + dt * 0) &
            (self.df.date <= date.date() + dt * 6)
        ]

        # At a 10-minute collection interval, the number of points
        # collected per day is 144.
        # If we don't have 144 then obviously something's missing
        datapoints = 0 # 86400 / 600 * 7
        datapoints = max(datapoints, len(week_df))

        base_diff = datapoints - len(week_df)
        num_on = len(week_df[week_df.display == 'on'])

        frac = (base_diff + num_on) / datapoints
        return rounded(frac * 100)

    def by_weekday_and_hour(self, day=None, hour=None):
        if day is not None:
            if isinstance(day, list):
                day_df = self.df[self.df.weekday.isin(day)]
            else:
                day_df = self.df[self.df.weekday == day]
        else:
            day_df = self.df

        if hour is not None:
            hour_df = day_df[
                (day_df.hour >= hour) &
                (day_df.hour < hour + 1)]
        else:
            hour_df = day_df

        return self.__class__(hour_df)
