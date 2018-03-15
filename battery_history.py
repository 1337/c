#!/usr/bin/env python3

import csv
import datetime
import matplotlib.pyplot as plt

try:
    f = open('battery_history.csv', newline='')
except IOError:
    f = open('/home/brian/Downloads/battery_history.csv', newline='')

points = []
with f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        points.append(int(row[2].strip()))

plt.plot(points)
plt.axhline(y=80, linewidth=1, color='r')
plt.axhline(y=58, linewidth=1, color='g')
plt.axhline(y=40, linewidth=1, color='g')
plt.show()
