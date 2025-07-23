import time
import requests
from flask import Flask
from threading import Thread
import random

TOKEN = '8038736203:AAECtnHYlibz6V5AtvdnjdVaebGsx-UV_eU'
CHANNEL_ID = '@gowinst'

def generate_grid(rows=5, cols=5, stars=5):
    grid = [['🟦' for _ in range(cols)] for _ in range(rows)]
    positions = random.sample([(r, c) for r in range(rows) for c in range(cols)], stars)
    for r, c in positions:
        grid[r][c] = '⭐️'
    return '\n'.join([''.join(row) for row in grid])

def create_message():
    grid = generate_grid()
    message = (
        "✅ تأكيد الدخول!\n\n"
        "💣 القنابل: 3\n"
        "🎯 المحاولات: 3\n\n"
        "🎮 اضغط هنا وابدأ اللعب!\n\n"
        f"{grid}\n\n"
        "🔍 تابع الشرح لمزيد من التفاصيل"
    )
    return message

def send_messages():
    while True:
        message = create_message()
        text_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHANNEL_ID, "text": message}
        requests.post(text_url, data=payload)

        time.sleep(120)

        sticker_id = "CAACAgIAAxkBAAEPAAFQaIA6Ps2XYKQimobPYq1DjExfNbsAAoAnAAKcNlhLRE8QLYjGSRw2BA"
        sticker_url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
        sticker_payload = {"chat_id": CHANNEL_ID, "sticker": sticker_id}
        requests.post(sticker_url, data=sticker_payload)

        time.sleep(180)

app = Flask('')

@app.route('/')
def home():
    return "البوت شغال"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
send_messages()
