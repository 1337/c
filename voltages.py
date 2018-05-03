#!/usr/bin/env python3

import matplotlib.pyplot as plt

import reader


def plot(df, canvas):
    df = df[df.voltage > 0]

    canvas.scatter(
        df.percent,
        df.Voltage,
        s=3,
        c='green',
        alpha=0.2)
    canvas.set_xlabel('Battery percent')
    canvas.set_ylabel('Voltage (V)')
    canvas.legend(loc='upper left')
    canvas.set_title('Battery voltage by capacity')

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
