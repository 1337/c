#!/usr/bin/env python3

import tabulate

import reader

tabulate.PRESERVE_WHITESPACE = True

df = reader.read_battery_history()
overall_analyzer = reader.Analyzer(df)

last_31_days_df = reader.get_last_31_days(df)
last_31_analyzer = reader.Analyzer(last_31_days_df)

rows = [
    [None, 'Lifetime', 'Last 31 days'],
    ['Data points', len(overall_analyzer.df)],
    ['Days', overall_analyzer.days],
    ['Charge events',
     overall_analyzer.charge_events,
     last_31_analyzer.charge_events],
    ['Discharge events',
     overall_analyzer.discharge_events,
     last_31_analyzer.discharge_events],
    ['Times charged to 100%',
     overall_analyzer.charging_to_100_times,
     last_31_analyzer.charging_to_100_times],
    ['Times charged to 90%',
     overall_analyzer.charging_to_90_times,
     last_31_analyzer.charging_to_90_times],
    ['Time spent between 20%~80% (%)',
     overall_analyzer.between_20_80_percent,
     last_31_analyzer.between_20_80_percent],
    ['Time spent between 45%~58% (%)',
     overall_analyzer.between_44_58_percent,
     last_31_analyzer.between_44_58_percent],
    ['Average screen on per day (%)',
     overall_analyzer.screen_on_percent,
     last_31_analyzer.screen_on_percent],

    # "\t" won't tabulate well because it's retarded
    ['  - Mondays',
     overall_analyzer.screen_on_percent_by_day(0),
     last_31_analyzer.screen_on_percent_by_day(0)],
    ['  - Tuesdays',
     overall_analyzer.screen_on_percent_by_day(1),
     last_31_analyzer.screen_on_percent_by_day(1)],
    ['  - Wednesdays',
     overall_analyzer.screen_on_percent_by_day(2),
     last_31_analyzer.screen_on_percent_by_day(2)],
    ['  - Thursdays',
     overall_analyzer.screen_on_percent_by_day(3),
     last_31_analyzer.screen_on_percent_by_day(3)],
    ['  - Fridays',
     overall_analyzer.screen_on_percent_by_day(4),
     last_31_analyzer.screen_on_percent_by_day(4)],
    ['  - Saturdays',
     overall_analyzer.screen_on_percent_by_day(5),
     last_31_analyzer.screen_on_percent_by_day(5)],
    ['  - Sundays',
     overall_analyzer.screen_on_percent_by_day(6),
     last_31_analyzer.screen_on_percent_by_day(6)],
    ['Average voltage (V)', overall_analyzer.average_voltage,
     last_31_analyzer.average_voltage],
]

print(tabulate.tabulate(rows))
