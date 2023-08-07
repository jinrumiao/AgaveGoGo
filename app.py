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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()
