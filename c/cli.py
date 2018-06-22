#!/usr/bin/env python3

# coding=utf-8

import click

from .battery_history import main as battery_history
from .overview import main as overview
from .percent_cumulative_distribution import main as percent_cumulative_distribution
from .percent_distribution import main as percent_distribution
from .screen_on_week import main as screen_on_week
from .stats import main as stats
from .time_of_day import main as time_of_day
from .time_of_weekday import main as time_of_weekday
from .voltages import main as voltages


THINGS_YOU_CAN_RUN = [
    'battery_history',
    'overview',
    'percent_cumulative_distribution',
    'percent_distribution',
    'screen_on_week',
    'stats',
    'time_of_day',
    'time_of_weekday',
    'voltages',
]


@click.command()
@click.argument('subcommand',
                default='overview',
                nargs=1,
                type=click.Choice(THINGS_YOU_CAN_RUN))
def main(subcommand):
    if subcommand == 'battery_history':
        battery_history()
    elif subcommand == 'overview':
        overview()
    elif subcommand == 'percent_cumulative_distribution':
        percent_cumulative_distribution()
    elif subcommand == 'percent_distribution':
        percent_distribution()
    elif subcommand == 'screen_on_week':
        screen_on_week()
    elif subcommand == 'stats':
        stats()
    elif subcommand == 'time_of_day':
        time_of_day()
    elif subcommand == 'time_of_weekday':
        time_of_weekday()
    elif subcommand == 'voltages':
        voltages()
    else:
        raise ValueError('No option %s' % subcommand)


if __name__ == '__main__':
    main()
