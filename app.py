from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask(__name__)

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
    message_text = str(event.message.text).lower()

    # ############"使用說明"############
    if message_text == "@使用說明":
        about_us_event(event)
        Usage(event)

    # ############"油價查詢"############
    if message_text == "油價查詢":
        content = oil_price()
        line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(content)
        )

    # ############"@小幫手"############
    if message_text == "@小幫手":
        button_template = Template_msg()
        line_bot_api.reply_message(
        event.reply_token, button_template
        )


@handler.add(FollowEvent)
def handle_follow(event):
    emojis = [
        {
            "index": 0, 
            "productId": "5ac21a18040ab15980c9b43e", 
            "emojiId": "009"
        }, 
        {
            "index": 16, 
            "productId": "5ac21a18040ab15980c9b43e", 
            "emojiId": "014"
        }
    ]

    welcome_message = TextSendMessage(text='''$ Agave Finance $
    您好，歡迎加入成為 Agave Finance 的好友!!!
    我是Agave財經小幫手~
    下方選單有：
    股票查詢、油價查詢、匯率查詢、自動提醒、資訊整理、使用說明
    使用上有任何問題可以參考使用說明''', emojis=emojis)

    line_bot_api.reply_message(
        event.reply_token, welcome_message
        )
    

@handler.add(UnfollowEvent)
def hadle_unfollow(event):
    print(event)


if __name__ == "__main__":
    app.run()
