import random
import keys
import os
import prefs
import webbrowser
import time
import calculate

class DoubleA():
    sillyState = False

    def __init__(self):
        prefs.load()
        
        print("Bot initialized!\n")
        greeting = random.choice(keys.greetings)
        if greeting == "Hello there.":
            self.sillyState = True
        print(greeting.replace('$name$', prefs.data["name"]))
        
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

        elif query == keys.say_name_condition:
            print("Your name is " + prefs.data["name"] + ".")

        elif query == keys.scatter_condition:
            calculate.scatter()

        elif query == keys.mean_condition:
            calculate.mean()

        elif query == keys.math_condition:
            calculate.calculate()

        else:
            print(random.choice(keys.confused_responses))
