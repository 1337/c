# C

This is a battery history analyZer for android and compatible systems.

The package includes library functions for extracting battery data from
collections of CSV files, as well as a helper CLI to generate charts
from the terminal.

## Installing

This is a python 3 package, and requires python 3.5.
To install, type in the terminal:

    pip3 install c

## Configuration

There is nothing to configure in this package, but you must configure
your android device to output CSV files in this format:

    YYYY-MM-DD,HH.mm,!C,!D,!V

Special formats are defined as follows:

* `!C`: the capacity ("percentage") of your battery at the time, from
  0 to 100.
* `!D`: whether your screen was on at the time, as `on` or `off`.
* `!V`: the voltage of your battery, in microvolts. `4000000` means 4V.

The device *must* append a new entry every 10 minutes, specifically,
whenever the time's minute mod 10 is 0.

## Running

To see all graphs:

    $ c overview

To see individual graphs:

    $ c that_graph_name  # listed in cli.py

To see just the stats:

    $ c stats
    ------------------------------  -------------  ------------  ---------
                                    Last 395 days  Last 30 days  Last week
    Data points                     52529          4165          826
    Times charged to 100%           24             0             0
    Times charged to 90%            72             14            0
    Times charged to 80%            185            16            0
    Time spent between 20%~80% (%)  94.26          92.29         100.0
    Time spent between 45%~58% (%)  41.43          42.3          68.64
    Average voltage (V)             3.88           3.91          3.91
    Charge events*                  2344           134           37
    Discharge events*               1305           74            18

    Screen on per day (hrs)         7.63           2.63          1.74
      - Mondays                     7.5            3.17          0.33
      - Tuesdays                    7.35           1.5           0.83
      - Wednesdays                  6.81           1.79          0.83
      - Thursdays                   7.4            3.0           1.67
      - Fridays                     6.94           2.42          1.52
      - Saturdays                   8.26           3.9           5.65
      - Sundays                     9.23           2.72          4.11
    ------------------------------  -------------  ------------  ---------

## Name

C is one of the characters in one of my grandparents' names.

## LicenSe

This project is licenSed under the GPL v3 licenSe.

## Changelog

### 0.0.6

Save figures only if the `figs` directory is available.
Fix issue with blank files.

### 0.0.5

Fix command line when handling 'stats'.

### 0.0.3

Add an actual command line.

### 0.0.2

Fix execution in virtual envs with imports in relative paths.

### 0.0.1

Initial release.
