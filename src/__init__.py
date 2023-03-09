import chatter
import client
import keys

bot = chatter.DoubleA()
client.startLog()

while True:
    query = input("\n> ")

    if query in keys.exit_conditions:
        break
    else:
        try:
            bot.chat(query)
        except Exception as Argument:
            client.log(Argument)
