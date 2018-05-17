#!/usr/bin/env python3

import tabulate

from common import rounded
import reader

tabulate.PRESERVE_WHITESPACE = True


def main(df):
    overall_analyzer = reader.Analyzer(df)

    last_30_days_df = reader.get_last_30_days(df)
    last_30_analyzer = reader.Analyzer(last_30_days_df)

    last_7_days_df = reader.get_last_7_days(df)
    last_7_analyzer = reader.Analyzer(last_7_days_df)

    rows = [
        [None,
        'Last {} days'.format(overall_analyzer.days),
        'Last 30 days',
        'Last week',
        ],
        ['Data points',
        len(overall_analyzer.df),
        len(last_30_analyzer.df),
        len(last_7_analyzer.df),
        ],
        ['Times charged to 100%',
        overall_analyzer.charging_to_100_times,
        last_30_analyzer.charging_to_100_times,
        last_7_analyzer.charging_to_100_times],
        ['Times charged to 90%',
        overall_analyzer.charging_to_90_times,
        last_30_analyzer.charging_to_90_times,
        last_7_analyzer.charging_to_90_times],
        ['Times charged to 80%',
        overall_analyzer.charging_to_80_times,
        last_30_analyzer.charging_to_80_times,
        last_7_analyzer.charging_to_80_times],
        ['Time spent between 20%~80% (%)',
        overall_analyzer.between_20_80_percent,
        last_30_analyzer.between_20_80_percent,
        last_7_analyzer.between_20_80_percent],
        ['Time spent between 45%~58% (%)',
        overall_analyzer.between_44_58_percent,
        last_30_analyzer.between_44_58_percent,
        last_7_analyzer.between_44_58_percent],
        ['Average voltage (V)',
        overall_analyzer.average_voltage,
        last_30_analyzer.average_voltage,
        last_7_analyzer.average_voltage,
        ],
        ['Charge events*',
        overall_analyzer.charge_events,
        last_30_analyzer.charge_events,
        last_7_analyzer.charge_events,
        ],
        ['Discharge events*',
        overall_analyzer.discharge_events,
        last_30_analyzer.discharge_events,
        last_7_analyzer.discharge_events,
        ],

        [None],  # Separator

        ['Screen on per day (hrs)',
        rounded(overall_analyzer.screen_on_percent * 0.24),
        rounded(last_30_analyzer.screen_on_percent * 0.24),
        rounded(last_7_analyzer.screen_on_percent * 0.24)],

        # "\t" won't tabulate well because it's retarded
        ['  - Mondays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(0) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(0) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(0) * 0.24),
        'M'],
        ['  - Tuesdays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(1) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(1) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(1) * 0.24),
        'T'],
        ['  - Wednesdays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(2) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(2) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(2) * 0.24),
        'W'],
        ['  - Thursdays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(3) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(3) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(3) * 0.24),
        'T'],
        ['  - Fridays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(4) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(4) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(4) * 0.24),
        'F'],
        ['  - Saturdays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(5) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(5) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(5) * 0.24),
        'S'],
        ['  - Sundays',
        rounded(overall_analyzer.screen_on_percent_by_weekday(6) * 0.24),
        rounded(last_30_analyzer.screen_on_percent_by_weekday(6) * 0.24),
        rounded(last_7_analyzer.screen_on_percent_by_weekday(6) * 0.24),
        'S'],
    ]

    print(tabulate.tabulate(rows))
    print('* Not accurate. If it were then the two values would match.')


if __name__ == '__main__':
    df = reader.read_battery_history()
    main(df)