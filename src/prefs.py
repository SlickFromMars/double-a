import os
import json
from appdata import AppDataPaths

app_paths = AppDataPaths('DoubleA')
app_paths.setup()

path = app_paths.app_data_path + '/prefs.json'

data = {
    "name": "User"
}

def save():
    global data

    f = open(path, 'w')
    f.write(json.dumps(data))
    f.close()


def load():
    global data

    tempData = data

    if (os.path.isfile(os.path.abspath(path))):
        f = open(path, 'r')
        raw = f.read()
        tempData = json.loads(raw)
        f.close()
        print("Loaded preferences!")

    for key in tempData.keys():
        data[key] = tempData[key]
