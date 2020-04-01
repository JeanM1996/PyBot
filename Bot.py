# bot.py
import requests  
import os
from flask import Flask, request# Add your telegram token as environment variable
BOT_URL = f'https://api.telegram.org/bot{os.environ["telekey"]}/'


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json

    print(data)  # Comment to hide what Telegram is sending you
    chat_id = data['message']['chat']['id']
    user_name=data['message']['from']['first_name']
    message = data['message']['text']


    if '/start'in message.lower():
         messageS="Bienvenido, dime Hola y te saludare o covid y te informaré el número de casos reportados en Ecuador"

    if 'hola'in message.lower():
         messageS="Hola "+user_name

    if 'covid'in message.lower():
         messageS="Según el reporte del MSP en el Ecuador hay 2748 casos"


    json_data = {
        "chat_id": chat_id,
        "text": messageS,
    }
    

    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=json_data)

    return ''


if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)