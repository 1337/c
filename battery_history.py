#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader

df = reader.read_battery_history()

plt.plot(df.percent)
plt.axhline(y=80, linewidth=1, color='r')
plt.axhline(y=58, linewidth=1, color='g')
plt.axhline(y=40, linewidth=1, color='g')
plt.show()
