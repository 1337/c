# C

This is a battery history analyZer for android and compatible systems.

## Configuration

There is nothing to configure in this package, but you must configure
your android device to output CSV files in this format:

    YYYY-MM-DD,HH.mm,!C,!D,!V

Special formats are defined as follows:

* `!C`: the capacity ("percentage") of your battery at the time, from
  0 to 100.
* `!D`: whether your screen was on at the time, as `on` or `off`.
* `!V`: the voltage of your battery, in microvolts. `4000000` means 4V.

## Running

To see all graphs:

    c overview

To see individual graphs:

    c that_graph_name  # listed in cli.py

## Changelog

### 0.0.5

Fix command line when handling 'stats'.

### 0.0.3

Add an actual command line.

### 0.0.2

Fix execution in virtual envs with imports in relative paths.

### 0.0.1

Initial release.
