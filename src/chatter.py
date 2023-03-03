import random
import keys
import os
import prefs

class DoubleA():
    def __init__(self):
        prefs.save("test", "test")
        
        print("Bot initialized!")
        
    def chat(self, query):
        if query.startswith(keys.project_condition):
            project = query.replace(keys.project_condition, "")
            path = os.path.expanduser("~/Documents/GitHub/" + project)
            if(os.path.isdir(path)):
                print("Opening " + project + "...")
                os.system("code " + path)
            else:
                print(path + " is not a directory!")
        else:
            print(random.choice(keys.confused_responses))