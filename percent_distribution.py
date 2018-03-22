#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


df = reader.read_battery_history()
values = df.percent.value_counts()

ys = []
for idx in range(100):
    try:
        ys.append(values[idx])
    except KeyError:
        ys.append(0)

plt.plot(range(100), ys)
plt.show()
