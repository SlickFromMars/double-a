import json
import os

data = {"name": "User", "speechEnabled": True}

data_path: str
prefs_path: str


def setup():
    global data_path
    global prefs_path
    data_path = os.path.join(os.path.expanduser("~"), ".doublea")
    prefs_path = os.path.join(data_path, "prefs.json")

    os.makedirs(data_path, exist_ok=True)


def save():
    global data
    global prefs_path

    f = open(prefs_path, "w")
    f.write(json.dumps(data, indent=4))
    f.close()


def load():
    global data
    global prefs_path

    tempData = data

    if os.path.isfile(os.path.abspath(prefs_path)):
        f = open(prefs_path, "r")
        raw = f.read()
        tempData = json.loads(raw)
        f.close()
        print("Loaded preferences!")

    for key in tempData.keys():
        data[key] = tempData[key]
