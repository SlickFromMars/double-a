import chatter
import keys

bot = chatter.DoubleA()

while True:
    query = input('\n> ').lower()
    
    if query in keys.exit_conditions:
        break
    else:
        bot.chat(query)