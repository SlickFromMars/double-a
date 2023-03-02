import random
import keys
import os

class DoubleA():
    def __init__(self):
        print("Bot initialized!")
        
    def chat(self, query):
        if query.startswith(keys.project_condition):
            project = query.replace(keys.project_condition, "")
            path = os.path.expanduser("~/Documents/GitHub/" + project)
            if(os.path.isdir(path)):
                print("Opening " + project + "...")
                os.system("code " + path)
                os.system("github " + path)
            else:
                print(path + " is not a directory!")
        else:
            print(random.choice(keys.confused_responses))