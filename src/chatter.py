import random
import keys
import prefs
import webbrowser
import time
import calculate
import project

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

        elif query.startswith(keys.name_condition):
            name = query.replace(keys.name_condition, "")
            prefs.data["name"] = name
            print("Hello, " + name + "!")
            prefs.save()

        elif query == keys.say_name_condition:
            print("Your name is " + prefs.data["name"] + ".")

        elif query == "Open a project.":
            project.open_project()

        elif query == "Generate scatter plot.":
            calculate.scatter()

        elif query == "Calculate mean.":
            calculate.mean()

        elif query == "Solve a math problem.":
            calculate.calculate()

        elif query == "Generate pie chart.":
            calculate.pie()

        elif query == "Generate bar graph.":
            calculate.bar()

        else:
            print(random.choice(keys.confused_responses))
