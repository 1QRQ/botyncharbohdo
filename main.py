import time
import requests
from flask import Flask
from threading import Thread
import random

# بيانات البوت
TOKEN = '7959797318:AAFIZreFesOIa-BRrES5W3ZvL6Z-freBUoE'
CHANNEL_ID = '@gowinst'

# File IDs
STICKERS = [
    "CAACAgIAAxkBAAEPAAFQaIA6Ps2XYKQimobPYq1DjExfNbsAAoAnAAKcNlhLRE8QLYjGSRw2BA",
    "CAACAgIAAxkBAAEO4Gxoa_iXoX8T5Ymf3SwP6x2KQefJIAACAwEAAladvQoC5dF4h-X6TzYE"
]
IMAGE_ID = "AgACAgQAAxkBAAMEaIFCOUAEMlyckKZq-CkMe014bm0AAozLMRuV1AlQmz1UmiG_RBIBAAMCAANzAAM2BA"
IMAGE_ID_2 = "AgACAgQAAxkBAAMSaJIpOwrUxroY_wWcwYIMp5lQhxAAAkrSMRuVKZBQ1CuoXrEclgABAQADAgADeQADNgQ"

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
        " الفخاخ: 3 ✖️\n"
        "🎯 المحاولات: 3\n\n"
        "🎮 [👈🏻 ابدأ من هنا 👉🏻](https://1win.com.ci/v3/2158/1win-mines?p=kquw)\n\n"
        f"{grid}\n\n"
        "[📩 لتواصل](https://t.me/Faridsupp1)"
    )

# إرسال الرسائل
def send_text(text, parse_mode="Markdown", reply_markup=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    if reply_markup:
        data["reply_markup"] = reply_markup
    requests.post(url, json=data)

def send_sticker(sticker_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
    data = {"chat_id": CHANNEL_ID, "sticker": sticker_id}
    requests.post(url, data=data)

def send_photo(photo_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {"chat_id": CHANNEL_ID, "photo": photo_id}
    requests.post(url, data=data)

# الدور الرئيسي
def send_loop():
    sticker_index = 0
    last_image_time = time.time()
    last_image2_time = time.time()

    while True:
        send_text("🚨 _جاري ربط خوارزميات موقع 1وين بالقناة_", parse_mode="Markdown")
        time.sleep(5)

        # نشر الرسالة الرئيسية
        msg = create_message()
        send_text(
            msg,
            reply_markup={
                "inline_keyboard": [
                    [{"text": "👈🏻 افتح اللعبة 👉🏻", "url": "https://1win.com.ci/casino/play/v_1winGames:Mines_classic?p=kquw"}]
                ]
            }
        )
        print("✅ تم نشر الرسالة.")

        time.sleep(5)

        # نشر رسالة العد التنازلي
        send_text("3 دقائق لتنتهي الجولة ... ✅")
        print("⌛ تم نشر رسالة العد التنازلي.")

        time.sleep(185)  # 3 دقائق و5 ثواني

        # إرسال ستيكر بالتناوب
        send_sticker(STICKERS[sticker_index])
        sticker_index = (sticker_index + 1) % len(STICKERS)
        print("📎 تم إرسال ستيكر.")

        # إرسال الصورة الأولى كل 25 دقيقة (1500 ثانية)
        if time.time() - last_image_time >= 1500:
            send_photo(IMAGE_ID)
            last_image_time = time.time()
            print("🖼️ تم إرسال صورة.")

        # إرسال الصورة الثانية كل 7 دقائق (420 ثانية)
        if time.time() - last_image2_time >= 420:
            send_photo(IMAGE_ID_2)
            last_image2_time = time.time()
            print("🖼️ تم إرسال الصورة الثانية.")

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

