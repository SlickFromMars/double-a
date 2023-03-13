import os

import requests

import keys
from speech import say


def git_project():
    project = input("Project name > ")
    project = project.replace(" ", "-")
    path = os.path.expanduser("~/Documents/GitHub/" + project)
    if os.path.isdir(path):
        say("Opening " + project + ".")
        os.system("code " + path)
        os.system("github " + path)
    else:
        say(path + " is not a directory!")


def show_license():
    r = requests.get(
        "https://raw.githubusercontent.com/SlickFromMars/double-a/main/LICENSE.txt"
    )
    if r:
        print("\n" + r.text)
        f = open(keys.license_path, "w")
        f.write(r.text)
    elif os.path.isfile(keys.license_path):
        say(
            str(r.status_code) + " Error getting online license. Showing local version."
        )
        f = open(keys.license_path, "r")
        print("\n" + f.read())
    else:
        say("Could not get license!")
