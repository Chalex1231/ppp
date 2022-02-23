
import telebot
from telebot import types

token = '5296921044:AAGb4JeYs5nvPq2wSs8SBagNSTYP3mAkQLw'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start']) 
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row( "/help", "/mtuci", "/Wikipedia" )
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать что я умею напиши /help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вот команды, которые я могу выполнить:\n/start - начать общение\n/help - команды, которые я могу выполнить\n/mtuci - сайт МТУСИ \n/Wikipedia - ссылка на энциклопедию"')


@bot.message_handler(commands=['Wikipedia'])
def start_message(message):
    bot.send_message(message.chat.id,'Wiki - https://ru.wikipedia.org')

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id,'Сайт МТУСИ – https://mtuci.ru/')


@bot.message_handler(content_types=['text'])
def answer(message):
    

    if message.text.lower() ==  "здравствуй":
      bot.send_message(message.chat.id, 'Добрый день')

    if message.text.lower() == "какое сейчас время года?":
      bot.send_message(message.chat.id, 'Сейчас зима, одевайтесь теплее')

    if message.text.lower() == "где можно посмотреть смешные видосики?":
      bot.send_message(message.chat.id, 'вот тут - https://www.youtube.com/c/Webmproject')
    
    
      
      
      
     


bot.polling(none_stop=True, interval=0)

