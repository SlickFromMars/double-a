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