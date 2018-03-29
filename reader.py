import datetime

import pandas as pd

from common import clean_voltage, rounded, str_to_date


def read_battery_history():
    """Add some processing"""
    df = pd.read_csv(
        open('battery_history.csv'),
        delimiter=',',
        header=None,  # "csv has no headers"
        names=['date', 'hour', 'percent', 'display', 'voltage'])

    # Map function to column, then put the column back (or another column)
    df['date'] = df['date'].apply(str_to_date)
    df['weekday'] = df['date'].apply(lambda x: x.isoweekday() - 1)
    df['hour'] = df['hour'].apply(float)
    df['percent'] = df['percent'].apply(int)
    df['percent_row_before'] = df['percent'].apply(int).shift(1)
    df['percent_row_after'] = df['percent'].apply(int).shift(-1)
    df['percent_7_day_rolling'] = df['percent'].rolling(window=1008).mean()
    df['percent_30_day_rolling'] = df['percent'].rolling(window=4320).mean()
    df['voltage'] = df['voltage'].apply(clean_voltage)

    return df


def get_last_30_days(df):
    _30_days_ago = (
        datetime.datetime.now() - datetime.timedelta(days=30)).date()
    return df[df.date >= _30_days_ago]


def get_between_20_80_times(df) -> int:
    return max(df[
        (20 <= df.percent) &
        (df.percent <= 80)].count())  # Conditions cannot be chained


def get_between_44_58_times(df) -> int:
    return max(df[
        (44 <= df.percent) &
        (df.percent <= 58)].count())  # Conditions cannot be chained


def get_charge_events(df) -> int:
    return max(df[
        (df.percent_row_before < df.percent) &
        (df.percent_row_after <= df.percent)].count())  # Inflection point


def get_discharge_events(df) -> int:
    return max(df[
        (df.percent_row_before > df.percent) &
        (df.percent_row_after > df.percent)].count())  # Not >= because 100% stays 100%


def get_charging_to_100_times(df) -> int:
    return max(df[
        (df.percent_row_before == df.percent) &
        (df.percent_row_after < df.percent) &
        (df.percent == 100)].count())


def get_charging_to_90_times(df) -> int:
    return max(df[
        (df.percent_row_before < 90) &
        (df.percent >= 90)].count())


def get_charging_to_80_times(df) -> int:
    return max(df[
        (df.percent_row_before < 80) &
        (df.percent >= 80)].count())


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
        return rounded(max(screen_on_df.count()) / len(self.df) * 100)

    def screen_on_percent_by_day(self, weekday):
        screen_on_df = self.df[self.df.display == 'on']
        return rounded(
            max(screen_on_df[screen_on_df.weekday == weekday].count()) /
            max(self.df[self.df.weekday == weekday].count()) * 100)

    def by_day_and_hour(self, day=None, hour=None):
        if day is not None:
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