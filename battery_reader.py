#!/usr/bin/env python3

import csv
import datetime

data_points = 0
now_capacity = None
charging = False
fully_charged = False
charged_to_90 = False
charge_cycles = 0
discharge_cycles = 0
charging_to_100_times = 0
charging_to_90_times = 0
between_20_80_times = 0
ons = 0
offs = 0
prev_row = None
screen_on_discharge_rates = []
screen_off_discharge_rates = []
screen_on_charge_rates = []
screen_off_charge_rates = []
start_date = None
end_date = datetime.datetime.now().date()
week_buckets = [[], [], [], [], [], [], []]
tod_buckets = [[], [], [], [], [], [], [], [], 
               [], [], [], [], [], [], [], [], 
               [], [], [], [], [], [], [], []]

def mean(numbers):
    return round(float(sum(numbers)) / max(len(numbers), 1), 2)

def average_on(entries):
    ons = [x for x in entries if 'on' in x]
    if not entries:
        return 0
    return len(ons)/len(entries)

def rounded(num):
    return round(num, 2)

try:
    f = open('battery_history.csv', newline='')
except IOError:
    f = open('/home/brian/Downloads/battery_history.csv', newline='')

with f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        data_points += 1

        if now_capacity is None:
            now_capacity = row[2]
            start_date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
            continue
        row_date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
        week_buckets[row_date.isoweekday() - 1].append(row[3].strip())
        
        if 20 <= int(now_capacity) <= 80:
            between_20_80_times += 1

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

        if int(row[2]) > 90:
            if not charged_to_90:
                charged_to_90 = True
                charging_to_90_times += 1
        else:
            if charged_to_90:
                charged_to_90 = False

        tod_buckets[int(float(row[1].strip()))].append(row[3])
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

days = (end_date - start_date).days
screen_on_discharge_rate = mean(screen_on_discharge_rates)
screen_off_discharge_rate = mean(screen_off_discharge_rates)

print('Data points:\t\t\t', data_points)
print('Days:\t\t\t\t', days)
print('Cycles:\t\t\t\t', charge_cycles, discharge_cycles, '(', rounded(charge_cycles / days), 'per day)')
print('Times charged to 100%:\t\t', charging_to_100_times)
print('Times charged to 90%:\t\t', charging_to_90_times)
print('Time spent between 20%~80%:\t', rounded(between_20_80_times / data_points))
print('Average screen on Overall:\t', rounded(ons / (ons + offs)))
print('\tMonday:\t\t\t', rounded(average_on(week_buckets[0])))
print('\tTuesday:\t\t', rounded(average_on(week_buckets[1])))
print('\tWednesday:\t\t', rounded(average_on(week_buckets[2])))
print('\tThursday:\t\t', rounded(average_on(week_buckets[3])))
print('\tFriday:\t\t\t', rounded(average_on(week_buckets[4])))
print('\tSaturday:\t\t', rounded(average_on(week_buckets[5])))
print('\tSunday:\t\t\t', rounded(average_on(week_buckets[6])))
print('Screen on by hour:')
for hour in range(24):
    print('\t{}:00:\t\t\t'.format(hour), 
          rounded(average_on(tod_buckets[hour])))
print('Screen on discharge rate:\t', screen_on_discharge_rate, '%/hr')
print('Screen off discharge rate:\t', screen_off_discharge_rate, '%/hr')
print('Screen on charge rate:\t\t', mean(screen_on_charge_rates), '%/hr')
print('Screen off charge rate:\t\t', mean(screen_off_charge_rates), '%/hr')
print('Nominal screen on time:\t\t', round(-60 / screen_on_discharge_rate, 0), 'hrs')
print('Nominal standby time:\t\t', round(-60 / screen_off_discharge_rate, 0), 'hrs')
