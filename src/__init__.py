import spacy

nlp = spacy.load("en_core_web_sm")
running = True
raw = ""

def run_ask():
    global raw
    raw = input('\nInput Command: ')
    
    my_doc = nlp(raw)
    print ([token.text for token in my_doc])

while running:
    run_ask()