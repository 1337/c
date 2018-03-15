#!/usr/bin/env python3

import datetime

try:
    f = open('battery_history.csv', newline='')
except IOError:
    f = open('/home/brian/Downloads/battery_history.csv', newline='')
    
outf = open('battery_history_out.csv', 'w')

with f:
    for line in f:
        outf.write(line.replace('\x00', ''))
