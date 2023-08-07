from line_bot_api import *
from events.basic import *

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


if __name__ == "__main__":
    app.run()
