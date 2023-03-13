import os
import random
import time
import webbrowser

import requests

import calculate
import client
import keys
from speech import say


class DoubleA:
    sillyState = False
    sussyChars = ".!?,"

    def greet(self):
        greeting_list = keys.greetings
        greeting_list.append("Hello there.")
        greeting = random.choice(greeting_list)
        if greeting == "Hello there.":
            self.sillyState = True
        say(greeting.replace("$name$", client.data["name"]))

    def __init__(self):
        client.load()

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
        
        elif trimmed_query == "Show code license":
            r = requests.get("https://raw.githubusercontent.com/SlickFromMars/double-a/main/LICENSE.txt")
            if r:
                print("\n" + r.text)
                f = open(keys.license_path, "w")
                f.write(r.text)
            elif os.path.isfile(keys.license_path):
                say(str(r.status_code) + " Error getting online license. Showing local version.")
                f = open(keys.license_path, "r")
                print("\n" + f.read())
            else:
                say("Could not get license!")

        elif trimmed_query.startswith("My name is "):
            name = trimmed_query.replace("My name is ", "")
            client.data["name"] = name
            say("Hello, " + name + "!")
            client.save()

        elif trimmed_query == "Say my name":
            say("Your name is " + client.data["name"] + ".")

        elif trimmed_query == "Open GitHub project":
            project = input("Project name > ")
            project = project.replace(" ", "-")
            path = os.path.expanduser("~/Documents/GitHub/" + project)
            if os.path.isdir(path):
                say("Opening " + project + ".")
                os.system("code " + path)
                os.system("github " + path)
            else:
                say(path + " is not a directory!")

        elif trimmed_query == "Generate scatter plot":
            calculate.scatter()

        elif trimmed_query == "Calculate mean":
            calculate.mean()

        elif trimmed_query == "Solve equation":
            calculate.calculate()

        elif trimmed_query == "Generate pie chart":
            calculate.pie()

        elif trimmed_query == "Generate bar graph":
            calculate.bar()

        elif trimmed_query == "Simplify radical":
            calculate.simp_rad()

        elif trimmed_query == "Calculate GCF":
            calculate.gcf()

        elif trimmed_query == "8-Ball":
            q = input("Ask your question. > ")
            time.sleep(random.randint(1, 3))
            say(random.choice(keys.ball_responses))
        
        elif trimmed_query == "Toggle speech":
            if client.data["speechEnabled"] == True:
                client.data["speechEnabled"] = False
                say("Disabled speech.")
            else:
                client.data["speechEnabled"] = True
                say("Enabled speech.")
            client.save()

        else:
            say(random.choice(keys.confused_responses))
