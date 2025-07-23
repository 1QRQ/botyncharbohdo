# إرسال الرسائل والستيكرات بدورة زمنية
def send_loop():
    while True:
        # إرسال المنشور الأول مع الزر
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

        # انتظار 5 ثواني ثم إرسال رسالة التنبيه
        time.sleep(5)
        notice_msg = "3 دقائق لتنتهي الجولة ... ✅"
        notice_data = {
            "chat_id": CHANNEL_ID,
            "text": notice_msg
        }
        requests.post(msg_url, data=notice_data)
        print("⏱️ تم إرسال إشعار الجولة.")

        # انتظار باقي الدقيقتين (115 ثانية)
        time.sleep(115)

        # إرسال الستيكر
        sticker_id = "CAACAgIAAxkBAAEPAAFQaIA6Ps2XYKQimobPYq1DjExfNbsAAoAnAAKcNlhLRE8QLYjGSRw2BA"
        sticker_url = f"https://api.telegram.org/bot{TOKEN}/sendSticker"
        sticker_data = {"chat_id": CHANNEL_ID, "sticker": sticker_id}
        requests.post(sticker_url, data=sticker_data)
        print("📎 تم إرسال الستيكر.")

        # انتظار 3 دقائق إضافية
        time.sleep(180)
