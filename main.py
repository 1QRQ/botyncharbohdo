import time
import requests
from flask import Flask
from threading import Thread
import random

# بيانات البوت
TOKEN = '7959797318:AAFIZreFesOIa-BRrES5W3ZvL6Z-freBUoE'
CHANNEL_ID = '@gowinst'

# إنشاء شبكة النجوم
def generate_grid(rows=5, cols=5, stars=4):
    grid = [['🟦' for _ in range(cols)] for _ in range(rows)]
    positions = random.sample([(r, c) for r in range(rows) for c in range(cols)], stars)
    for r, c in positions:
        grid[r][c] = '⭐️'
    return '\n'.join([''.join(row) for row in grid])

# توليد الرسالة
def create_message():
    grid = generate_grid()
    return (
        "✅ تأكيد الدخول!\n\n"
        "✖️ الفخاخ: 3\n"
        "🎯 المحاولات: 3\n\n"
        "🎮 [ابدأ من هنا](https://cutt.ly/1win_registration)\n\n"
        f"{grid}\n\n"
        "[لتواصل](https://t.me/Faridsupp1)\n\n"
    )

# إرسال الرسائل والستيكرات بدورة زمنية
def send_loop():
    while True:
        # إرسال المنشور الأساسي
        msg = create_message()
        msg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        msg_data = {
            "chat_id": CHANNEL_ID,
            "text": msg,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
            "reply_markup": {
                "inline_keyboard": [
                    [{"text": "👈🏻 افتح اللعبة 👉🏻", "url": "https://1win.com.ci/v3/2158/1win-mines?p=kquw"}]
                ]
            }
        }
        requests.post(msg_url, json=msg_data)
        print("✅ تم نشر الرسالة مع الزر.")

        # بعد 5 ثواني، إرسال إشعار الجولة
        time.sleep(5)
        notice_data = {
            "chat_id": CHANNEL_ID,
            "text": "3 دقائق لتنتهي الجولة ... ✅"
        }
        requests.post(msg_url, data=notice_data)
        print("⏱️ تم إرسال إشعار الجولة.")

        # انتظار 3 دقائق و 5 ثواني بعد رسالة الإشعار
        time.sleep(185)

        # إرسال الستيكر
        sticker_id = "CAACAgIAAxkBAAEPAAFQaIA6Ps2XYKQimobPYq1DjExfNbsAAoAnAAKcNlhLRE8QLYjGSRw2BA"
        sticker_url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
        sticker_data = {"chat_id": CHANNEL_ID, "sticker": sticker_id}
        requests.post(sticker_url, data=sticker_data)
        print("📎 تم إرسال الستيكر.")

        # انتظار 3 دقائق إضافية
        time.sleep(180)

# إبقاء البوت شغال في Railway
app = Flask('')

@app.route('/')
def home():
    return "✅ البوت يعمل بنجاح"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run).start()

# تشغيل الخادم والبوت
keep_alive()
send_loop()
