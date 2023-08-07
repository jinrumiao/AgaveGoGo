from line_bot_api import *


def about_us_event(event):
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

    sticker_message = StickerSendMessage(
        package_id="11537", sticker_id="52002735"
    )

    line_bot_api.reply_message(
        event.reply_token, 
        [welcome_message, sticker_message]
    )
