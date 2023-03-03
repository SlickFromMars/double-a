import random
import keys
import prefs
import webbrowser
import time
import calculate
import project

class DoubleA():
    sillyState = False
    sussyChars = ".!?,"

    def greet(self):
        greeting_list = keys.greetings
        greeting_list.append("Hello there.")
        greeting = random.choice(greeting_list)
        if greeting == "Hello there.":
            self.sillyState = True
        print(greeting.replace('$name$', prefs.data["name"]))

    def __init__(self):
        prefs.load()
        
        print("Bot initialized!\n")
        self.greet()
        
    def chat(self, query):
        trimmed_query = query.strip()
        if trimmed_query[len(trimmed_query) - 1] in self.sussyChars:
            trimmed_query = trimmed_query.rstrip(trimmed_query[-1])

        if self.sillyState and query.startswith("General Kenobi"):
            print("You are a bold one.")
            time.sleep(2)
            webbrowser.open("https://www.youtube.com/watch?v=rEq1Z0bjdwc")
            self.sillyState = False
            return
            
        elif self.sillyState:
            self.sillyState = False
        
        if query in keys.greet_conditions:
            self.greet()

        elif trimmed_query.startswith("My name is "):
            name = trimmed_query.replace("My name is ", "")
            prefs.data["name"] = name
            print("Hello, " + name + "!")
            prefs.save()

        elif query == "Say my name.":
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
