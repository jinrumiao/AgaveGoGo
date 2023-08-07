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

    if message_text == "@使用說明":
        about_us_event(event)
        Usage(event)

    if message_text == "@小幫手":
        Template_msg(event)


if __name__ == "__main__":
    app.run()
