from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '8065007276:AAGM5_qHN7W_DVdmewlHUPZPXx_7p0hTTE8'
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
        requests.post(TELEGRAM_API_URL, json={'chat_id': chat_id, 'text': reply})
    return {'ok': True}