import datetime
import json
import os

data_path = os.path.join(os.path.expanduser('~'), ".doublea")
prefs_path = os.path.join(data_path, "prefs.json")
log_path = os.path.join(data_path, "log.txt")

os.makedirs(data_path, exist_ok = True)

data = {"name": "User", "speechEnabled": True}

def save():
    global data

    f = open(prefs_path, "w")
    f.write(json.dumps(data))
    f.close()


def load():
    global data

    tempData = data

    if os.path.isfile(os.path.abspath(prefs_path)):
        f = open(prefs_path, "r")
        raw = f.read()
        tempData = json.loads(raw)
        f.close()
        print("Loaded preferences!")

    for key in tempData.keys():
        data[key] = tempData[key]

def log(e):
    d = datetime.time()
    f = open(log_path, "a")
    f.write(str(d) + " - " + str(e) + "\n")
    f.close()
    print(e + "\nSaved in " + log_path)

def startLog():
    if(os.path.exists(log_path)):
        os.remove(log_path)
    
    f = open(log_path, "w")
    f.write("Bot started!")
    f.close()