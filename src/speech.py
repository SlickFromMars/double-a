import pyttsx3 as tts

import client

engine:tts.Engine

def setup():
    global engine
    engine = tts.init()

def say(txt:str):
    print(txt)
    if client.data["speechEnabled"] == True:
        if engine.isBusy():
            engine.stop()
        engine.say(txt)
        engine.runAndWait()