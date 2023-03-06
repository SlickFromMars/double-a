import os
import random
import time
import webbrowser

import calculate
import keys
import prefs


class DoubleA:
    sillyState = False
    sussyChars = ".!?,"

    def greet(self):
        greeting_list = keys.greetings
        greeting_list.append("Hello there.")
        greeting = random.choice(greeting_list)
        if greeting == "Hello there.":
            self.sillyState = True
        print(greeting.replace("$name$", prefs.data["name"]))

    def __init__(self):
        prefs.load()

        print("Bot initialized!\n")
        self.greet()

    def chat(self, query):
        trimmed_query = query.strip()
        if trimmed_query[len(trimmed_query) - 1] in self.sussyChars:
            trimmed_query = trimmed_query.rstrip(trimmed_query[-1])

        if self.sillyState and trimmed_query == "General Kenobi":
            print("You are a bold one.")
            time.sleep(2)
            webbrowser.open("https://www.youtube.com/watch?v=rEq1Z0bjdwc")
            self.sillyState = False
            return

        elif self.sillyState:
            self.sillyState = False

        if trimmed_query in keys.greet_conditions:
            self.greet()

        elif trimmed_query.startswith("My name is "):
            name = trimmed_query.replace("My name is ", "")
            prefs.data["name"] = name
            print("Hello, " + name + "!")
            prefs.save()

        elif trimmed_query == "Say my name":
            print("Your name is " + prefs.data["name"] + ".")

        elif trimmed_query == "Open GitHub project":
            project = input("Project name > ")
            project = project.replace(" ", "-")
            path = os.path.expanduser("~/Documents/GitHub/" + project)
            if os.path.isdir(path):
                print("Opening " + project + "...")
                os.system("code " + path)
                os.system("github " + path)
            else:
                print(path + " is not a directory!")

        elif trimmed_query == "Generate scatter plot":
            calculate.scatter()

        elif trimmed_query == "Calculate mean":
            calculate.mean()

        elif trimmed_query == "Solve a math problem":
            calculate.calculate()

        elif trimmed_query == "Generate pie chart":
            calculate.pie()

        elif trimmed_query == "Generate bar graph":
            calculate.bar()

        else:
            print(random.choice(keys.confused_responses))
