import chatter
import client
import keys
import speech

client.setup()
speech.setup()
bot = chatter.DoubleA()

while True:
    query = input("\n> ")

    if query in keys.exit_conditions:
        break
    else:
        try:
            bot.chat(query)
        except Exception as Argument:
            print(Argument)
