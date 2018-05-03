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

    averages = []
    for percent in range(100):
        average = df[df.percent == percent].mean()['Voltage']
        averages.append(average)

    canvas.plot(range(100), averages)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plot(df=reader.read_battery_history(), canvas=ax)
    plt.show()
