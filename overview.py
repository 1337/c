#!/usr/bin/env python3

import matplotlib.pyplot as plt

import battery_history
import percent_cumulative_distribution
import percent_distribution
import reader
import screen_on_time


df = reader.read_battery_history()

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
battery_history.plot(df=df, canvas=ax1)
ax1.set_ylim([0, 100])

screen_on_time.plot(df=df, canvas=ax2)
ax2.set_xlim([0, 24])
ax2.set_ylim([0, 100])

percent_distribution.plot(df=df, canvas=ax3)
ax3.set_xlim([0, 100])
ax3.set_ylim([0, 8])

percent_cumulative_distribution.plot(df=df, canvas=ax4)
ax4.set_xlim([0, 100])
ax4.set_ylim([0, 100])

plt.show()
