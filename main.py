import time
import requests
from flask import Flask
from threading import Thread
import random

# ✅ معلومات البوت والقناة
TOKEN = '8038736203:AAECtnHYlibz6V5AtvdnjdVaebGsx-UV_eU'
CHANNEL_ID = '@gowinst'

# ✅ إنشاء شبكة الرموز
def generate_grid(rows=5, cols=5, stars=5):
    grid = [['🟦' for _ in range(cols)] for _ in range(rows)]
    positions = random.sample([(r, c) for r in range(rows) for c in range(cols)], stars)
    for r, c in positions:
        grid[r][c] = '⭐️'
    return '\n'.join([''.join(row) for row in grid])

# ✅ توليد الرسالة النصية
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

# ✅ المهمة الأساسية: نشر الرسالة ثم الستيكر
def send_messages():
    while True:
        # إرسال المنشور النصي
        text = create_message()
        send_text_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHANNEL_ID, "text": text}
        response = requests.post(send_text_url, data=payload)
        print("📤 منشور:", response.json())

        # انتظار 3 دقائق
        time.sleep(180)

        # إرسال الستيكر
        sticker_id = "CAACAgIAAxkBAAEPAAFQaIA6Ps2XYKQimobPYq1DjExfNbsAAoAnAAKcNlhLRE8QLYjGSRw2BA"
        sticker_url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
        payload = {"chat_id": CHANNEL_ID, "sticker": sticker_id}
        response = requests.post(sticker_url, data=payload)
        print("📎 ستيكر:", response.json())

        # انتظار دقيقتين إضافيتين (ليصبح الإجمالي 5 دقائق)
        time.sleep(120)

# ✅ تشغيل خادم Flask لإبقاء Railway نشطًا
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ البوت شغال 24/24"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ✅ تشغيل البوت
keep_alive()
send_messages()
