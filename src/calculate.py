import matplotlib.pyplot as plt
import numpy as np


def scatter():
    x = []
    y = []
    while True:
        x.append(input("Enter X coord > "))
        y.append(input("Enter Y coord > "))
        cont = input("Continue? (y/n)")
        if cont != "y":
            break

    plt.scatter(x, y)
    plt.show()


def pie():
    names = []
    values = []
    while True:
        names.append(input("Enter Label > "))
        values.append(input("Enter Value > "))
        cont = input("Continue? (y/n)")
        if cont != "y":
            break

    plt.pie(values, labels=names)
    plt.show()


def bar():
    names = []
    values = []
    while True:
        names.append(input("Enter Label > "))
        values.append(input("Enter Value > "))
        cont = input("Continue? (y/n)")
        if cont != "y":
            break

    plt.bar(names, values)
    plt.show()


def mean():
    raw = input("Enter list of numbers > ").replace(" ", "")
    grp = raw.split(",")
    tot = 0.0
    for i in grp:
        tot += float(i)
    x = tot / len(grp)
    print("Mean is " + str(x))


def calculate():
    raw = input("Enter problem > ")
    solved = eval(raw)
    print(solved)
