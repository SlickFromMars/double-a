import chatter
import keys

bot = chatter.DoubleA()

while True:
    query = input("\n> ")

    if query in keys.exit_conditions:
        break
    else:
        bot.chat(query)
