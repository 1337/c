#!/usr/bin/env python3

import matplotlib.pyplot as plt

import battery_history
import percent_cumulative_distribution
import percent_distribution
import reader
import screen_on_time_by_hour


f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)


df = reader.read_battery_history()
battery_history.plot(df=df, canvas=ax1)
screen_on_time_by_hour.plot(df=df, canvas=ax2)
percent_distribution.plot(df=df, canvas=ax3)
percent_cumulative_distribution.plot(df=df, canvas=ax4)

plt.show()
