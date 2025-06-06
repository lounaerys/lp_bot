import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет! Я умею определять, в каком созвездии сейчас находится планета. ' \
    'Для этого набери в чате команду /planet и название планеты на английском, например "/planet Mercury"')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_command(update, context):
    command_parts = update.message.text.split()

    if len(command_parts) < 2:
        return
    
    planet_name = command_parts[1].capitalize()

    if planet_name == 'Mars':
        planet = ephem.Mars()
    elif planet_name == 'Venus':
        planet = ephem.Venus()
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter()
    elif planet_name == 'Saturn':
        planet = ephem.Saturn()
    elif planet_name == 'Mercury':
        planet = ephem.Mercury()
    elif planet_name == 'Uranus':
        planet = ephem.Uranus()
    elif planet_name == 'Neptune':
        planet = ephem.Neptune()
    elif planet_name == 'Pluto':
        planet = ephem.Pluto()
    else:
        return
    
    planet.compute()
    constellation = ephem.constellation(planet)
    update.message.reply_text(f'Планета {planet_name} сейчас в созвездии {constellation}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_command))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   
    logging.info('Бот успешно запущен')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()