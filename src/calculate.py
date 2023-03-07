import math

import matplotlib.pyplot as plt


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

def getFactors(n):
    # Create an empty list for factors
    factors=[]

    # Loop over all factors
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # Return the list of factors
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
    if(e == 1.0):
        print(str(r))
    else:
        print(str(r) + " sqrt " + str(e))

def gcf():
    x = int(input("Number 1 > "))
    y = int(input("Number 2 > "))
    z = 1
    xf = getFactors(x)
    yf = getFactors(y)
    for i in xf:
        if i in yf:
            z = i
    print("GCF is " + str(z))