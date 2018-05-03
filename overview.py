#!/usr/bin/env python3

import matplotlib.pyplot as plt

import battery_history
import percent_cumulative_distribution
import percent_distribution
import reader
import screen_on_time
import voltages


df = reader.read_battery_history()

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
battery_history.plot(df=df, canvas=ax1)
ax1.set_ylim([0, 100])

screen_on_time.plot(df=df, canvas=ax2)
ax2.set_xlim([0, 24])
ax2.set_ylim([0, 100])

percent_distribution.plot(df=df, canvas=ax4)
ax4.set_xlim([0, 100])
ax4.set_ylim([0, 8])

percent_cumulative_distribution.plot(df=df, canvas=ax5)
ax5.set_xlim([0, 100])
ax5.set_ylim([0, 100])

voltages.plot(df=df, canvas=ax6)
ax6.set_xlim([0, 100])
ax6.set_ylim([3.4, 4.4])

plt.show()
