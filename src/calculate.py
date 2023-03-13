import math

import matplotlib.pyplot as plt

from speech import say


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
    say("Mean is " + str(x))


def calculate():
    raw = input("Enter problem > ")
    try:
        solved = eval(raw)
    except Exception as Argument:
        print(Argument)
    say(solved)


def getFactors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


def simp_rad():
    x = int(input("sqrt of > "))
    y = 0
    r = 0
    factors = getFactors(x)
    for i in factors:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            y = i
            r = root
    e = x / y
    if e == 1.0:
        say(str(r))
    else:
        say(str(r) + " sqrt " + str(e))


def gcf():
    x = int(input("Number 1 > "))
    y = int(input("Number 2 > "))
    z = 1
    xf = getFactors(x)
    yf = getFactors(y)
    for i in xf:
        if i in yf:
            z = i
    say("GCF is " + str(z))
