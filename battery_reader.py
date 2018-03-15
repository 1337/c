#!/usr/bin/env python3

import csv
import datetime
import pandas as pd
import tabulate


tabulate.PRESERVE_WHITESPACE = True


def str_to_date(x):
    if isinstance(x, datetime.date):
        return x
    return datetime.datetime.strptime(x, '%Y-%m-%d').date()


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
df['voltage'] = df['voltage'].apply(clean_voltage)


dow_buckets = [None] * 7
data_points = len(df)

between_20_80_times = max(df[
    (20 <= df.percent) & 
    (df.percent <= 80)].count())  # Conditions cannot be chained
between_45_58_times = max(df[
    (45 <= df.percent) & 
    (df.percent <= 58)].count())
charge_cycles = max(df[
    (df.percent_row_before < df.percent) & 
    (df.percent_row_after <= df.percent)].count())  # Inflection point
discharge_cycles = max(df[
    (df.percent_row_before > df.percent) & 
    (df.percent_row_after > df.percent)].count())  # Not >= because 100% stays 100%
charging_to_100_times = max(df[
    (df.percent_row_before == df.percent) & 
    (df.percent_row_after < df.percent) & 
    (df.percent == 100)].count())
charging_to_90_times = max(df[
    (df.percent_row_before < 90) & 
    (df.percent >= 90)].count())

average_voltage = int(df[df.voltage > 0].voltage.mean()) / 1000000

screen_on_df = df[df.display == 'on']
total_sot_percent = \
    max(screen_on_df.count()) / data_points * 100

for idx in range(7):
    dow_buckets[idx] = (
        max(screen_on_df[screen_on_df.weekday == idx].count())
        / max(df[df.weekday == idx].count())
    ) * 100

days = (df['date'].max() - df['date'].min()).days

rows = [
    ['Data points', data_points],
    ['Days', None, days],
    ['Charge cycles', charge_cycles, rounded(charge_cycles / days)],
    ['Discharge cycles', discharge_cycles, rounded(discharge_cycles / days)],
    ['Times charged to 100%', charging_to_100_times],
    ['Times charged to 90%', charging_to_90_times],
    ['Time spent between 20%~80% (%)', rounded(between_20_80_times / data_points * 100)],
    ['Time spent between 45%~58% (%)', rounded(between_45_58_times / data_points * 100)],
    ['Average screen on (%)', rounded(total_sot_percent)],
    ['    Monday', rounded(dow_buckets[0])],  # "\t" won't tabulate well because it's retarded
    ['    Tuesday', rounded(dow_buckets[1])],
    ['    Wednesday', rounded(dow_buckets[2])],
    ['    Thursday', rounded(dow_buckets[3])],
    ['    Friday', rounded(dow_buckets[4])],
    ['    Saturday', rounded(dow_buckets[5])],
    ['    Sunday', rounded(dow_buckets[6])],
    ['Average voltage (V)', rounded(average_voltage)],
]

print(tabulate.tabulate(rows))
