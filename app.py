from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler, exceptions
from linebot.exceptions import InvalidSignatureError
from linebot.models import *


app = Flask(__name__)

line_bot_api = LineBotApi("bobQ6mg/o0rZkBrYzuZ/DUKC3GrbqDqjMwf88EAjgbWqgGDejIRauFUMCiLC2gBGhQ5IhJSZSnNVEzsVUrln9VOk9DujR1v6zyCSXxvlBwUlhfNo7s6HyZH6Z0v2SCbHzC4OGtenkr+Tu+JSS6xDkAdB04t89/1O/w1cDnyilFU=")

handler = WebhookHandler("278f2f753e15266cf1b77462929c3f4a")


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    emojis = [
        {
            "index": 0, 
            "production": "5ac21a18040ab15980c9b43e", 
            "emojiId": "009"
        }, 
        {
            "index": 16, 
            "production": "5ac21a18040ab15980c9b43e", 
            "emojiId": "014"
        }
    ]

    welcome_message = TextSendMessage(text='''$ Agave Finance $
您好，歡迎加入成為 Agave Finance 的好友!!!
我是Agave財經小幫手~
下方選單有：
股票查詢、油價查詢、匯率查詢、自動提醒、資訊整理、使用說明
使用上有任何問題可以參考使用說明''', emojis=emojis)

    sticker_message = StickerSendMessage(
        package_id="11537", sticker_id="52002735"
    )

    line_bot_api.reply_message(
        event.reply_token, 
        [welcome_message, sticker_message]
    )


if __name__ == "__main__":
    app.run()
