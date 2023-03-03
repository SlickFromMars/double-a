import random
import keys
import os
import prefs
import random
import webbrowser
import time

class DoubleA():
    sillyState = False

    def __init__(self):
        prefs.load()
        
        print("Bot initialized!\n")
        greeting = random.choice(keys.greetings)
        if greeting == "Hello there":
            self.sillyState = True
        print(greeting + ", " + prefs.data["name"] + '! How can I help you today?')
        
    def chat(self, query):
        if self.sillyState:
            if query.startswith("General Kenobi"):
                print("You are a bold one.")
                time.sleep(2)
                webbrowser.open("https://www.youtube.com/watch?v=rEq1Z0bjdwc")
                return
            self.sillyState = False

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