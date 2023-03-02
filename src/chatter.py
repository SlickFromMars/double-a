import random
import keys

class DoubleA():
    def __init__(self):
        print("Bot initialized!")
        
    def chat(this, query):
        print(random.choice(keys.confused_responses))