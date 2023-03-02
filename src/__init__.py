import spacy

nlp = spacy.load("en_core_web_sm")
running = True
raw = ""

def run_ask():
    global raw

    raw = input('\nInput Command: ')
    print(raw)

while running:
    run_ask()