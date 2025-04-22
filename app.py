from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get('BOT_TOKEN')
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/')
def home():
    return 'Бот запущен и работает!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        reply = f"Ты написал: {text}"
        requests.post(URL, json={'chat_id': chat_id, 'text': reply})
    return {'ok': True}