import os

def open_project():
    project = input("Project name > ")
    path = os.path.expanduser("~/Documents/GitHub/" + project)
    if(os.path.isdir(path)):
        print("Opening " + project + "...")
        os.system("code " + path)
    else:
        print(path + " is not a directory!")