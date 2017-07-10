#!/usr/bin/env python3

import csv

now_capacity = None
charging = False
fully_charged = False
charge_cycles = 0
discharge_cycles = 0
charging_to_100_times = 0
ons = 0
offs = 0
prev_row = None
screen_on_discharge_rates = []
screen_off_discharge_rates = []
screen_on_charge_rates = []
screen_off_charge_rates = []

def mean(numbers):
    return round(float(sum(numbers)) / max(len(numbers), 1), 2)

try:
    f = open('battery_history.csv', newline='')
except IOError:
    f = open('/home/brian/Downloads/battery_history.csv', newline='')

with f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if now_capacity is None:
            now_capacity = row[2]
            continue

        if row[2] > now_capacity:
            # Capacity seen going up.
            if not charging:
                charging = True
                charge_cycles += 1
        elif row[2] < now_capacity:
            # Capacity seen going down.
            if charging:
                charging = False
                discharge_cycles += 1
        else:
            # Didn't change.
            pass
        
        if int(row[2]) == 100:
            if not fully_charged:
                fully_charged = True
                charging_to_100_times += 1
        else:
            if fully_charged:
                fully_charged = False

        if 'on' in row[3]:
            ons += 1
            if prev_row:
                rate = (float(row[2]) - float(prev_row[2])) * 6
                if charging:
                    screen_on_charge_rates.append(rate)
                else:
                    screen_on_discharge_rates.append(rate)
        elif 'off' in row[3]:
            offs += 1
            if prev_row:
                rate = (float(row[2]) - float(prev_row[2])) * 6
                if charging:
                    screen_off_charge_rates.append(rate)
                else:
                    screen_off_discharge_rates.append(rate)

        prev_row = row
        now_capacity = row[2]

screen_on_discharge_rate = mean(screen_on_discharge_rates)
screen_off_discharge_rate = mean(screen_off_discharge_rates)

print('Cycles:', charge_cycles, discharge_cycles)
print('Times charged to 100%:', charging_to_100_times)
print('On percentage:', round(ons * 100 / (ons + offs), 2))
print('Screen on discharge rate:', screen_on_discharge_rate, '%/hr')
print('Screen off discharge rate:', screen_off_discharge_rate, '%/hr')
print('Screen on charge rate:', mean(screen_on_charge_rates), '%/hr')
print('Screen off charge rate:', mean(screen_off_charge_rates), '%/hr')
print('Nominal screen on time:', round(-60 / screen_on_discharge_rate, 0), 'hrs')
print('Nominal standby time:', round(-60 / screen_off_discharge_rate, 0), 'hrs')
