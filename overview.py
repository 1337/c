#!/usr/bin/env python3

import arrow
import matplotlib.pyplot as plt

import battery_history
import percent_cumulative_distribution
import percent_distribution
import reader
import screen_on_week
import time_of_weekday
import time_of_day
import voltages


df = reader.read_battery_history()

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
battery_history.plot(df=df, canvas=ax1)
ax1.set_xlim([  # "show a week"
    arrow.now().replace(weeks=-1).datetime,
    arrow.now().datetime])
ax1.set_ylim([0, 100])

voltages.plot(df=df, canvas=ax2)
ax2.set_xlim([0, 100])
ax2.set_ylim([3.4, 4.4])

percent_distribution.plot(df=df, canvas=ax3)
ax3.set_xlim([0, 100])
ax3.set_ylim([0, 8])

screen_on_week.plot(df=df, canvas=ax4)
ax4.set_ylim([0, 18])

time_of_day.plot(df=df, canvas=ax5)
ax5.set_xlim([0, 24])
ax5.set_ylim([0, 80])

time_of_weekday.plot(df=df, canvas=ax6)
ax6.set_xlim([0, 24])
ax6.set_ylim([0, 80])

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1, hspace=0.3)
plt.show()
