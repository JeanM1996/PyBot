import os
import telebot
from flask import Flask, request

TOKEN = "817394076:AAE3x5yVKMytqLpknSfjN6WeKyCA10m3fz8"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

# Bot's Functionalitiesdef sendMessage(message, text):
bot.send_message(message.chat.id, text)# This method will send a message formatted in HTML to the user whenever it starts the bot with the /start command, feel free to add as many commands' handlers as you want@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Bienvenido🤖!</b>\n"
   "Escribe algo"
   )
bot.send_message(message.chat.id, text, parse_mode='HTML')# This method will fire whenever the bot receives a message from a user, it will check that there is actually a not empty string in it and, in this case, it will check if there is the 'hello' word in it, if so it will reply with the message we defined@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
   if 'hello'in message.text.lower():
      sendMessage(message, 'Hola, ¿Como estas?')