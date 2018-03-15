#!/usr/bin/env python3

import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    open('battery_history.csv'),
    delimiter=',',
    header=None,  # "csv has no headers"
    names=['date', 'hour', 'percent', 'display', 'voltage'])

df['percent'] = df['percent'].apply(int)

values = df.percent.value_counts()
ys = []
for idx in range(100):
    try:
        ys.append(values[idx])
    except KeyError:
        ys.append(0)

plt.plot(range(100), ys)
plt.show()
