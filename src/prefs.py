import os
import json

path = 'prefs.json'

data = {
    "name": "Slick"
}


def save():
    global data

    f = open('prefs.json', 'w')
    f.write(json.dumps(data))
    f.close()


def load():
    global data

    tempData = data

    if (os.path.isfile(os.path.abspath('prefs.json'))):
        f = open('prefs.json', 'r')
        raw = f.read()
        tempData = json.loads(raw)
        f.close()
        print("Loaded preferences!")

    for key in tempData.keys():
        data[key] = tempData[key]

    save()
