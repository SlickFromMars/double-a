import random
import keys
import os
import prefs
import random

class DoubleA():
    def __init__(self):
        prefs.load()
        
        print("Bot initialized!\n")
        print(random.choice(keys.greetings) + ", " + prefs.data["name"] + '! How can I help you today?')
        
    def chat(self, query):
        lowQuery = query.lower()
        if lowQuery.startswith(keys.project_condition):
            project = lowQuery.replace(keys.project_condition, "")
            path = os.path.expanduser("~/Documents/GitHub/" + project)
            if(os.path.isdir(path)):
                print("Opening " + project + "...")
                os.system("code " + path)
            else:
                print(path + " is not a directory!")
        elif query.startswith(keys.name_condition):
            name = query.replace(keys.name_condition, "")
            prefs.data["name"] = name
            print("Hello, " + name + "!")
            prefs.save()
        else:
            print(random.choice(keys.confused_responses))