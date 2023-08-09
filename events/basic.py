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

    button_template = Template_msg()

    line_bot_api.reply_message(
        event.reply_token, 
        [welcome_message, sticker_message, button_template]
    )


def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id, TextSendMessage(msg))


def Usage(event):
    push_msg(
        event, 
        """
        ℹ查詢方法ℹ
        🧞‍♂小幫手可以查詢股價、油價、匯率
        ➊股價查詢➡輸入股票代號
        ➋油價查詢➡輸入92、95、98、超柴
        ➌匯率查詢➡輸入國家
        ➍test
        ➎test
        ➏test
        """
    )


def Template_msg():
    button_template = TemplateSendMessage(
            alt_text="小幫手template", 
            template=ButtonsTemplate(
                title="選擇服務", 
                text="請選擇", 
                thumbnail_image_url="https://i.imgur.com/27uxIhZ.jpg", 
                actions=[
                    MessageTemplateAction(
                        label="股價查詢", 
                        text="股價查詢"
                    ), 
                    MessageTemplateAction(
                        label="油價查詢", 
                        text="油價查詢"
                    ), 
                    MessageTemplateAction(
                        label="匯率查詢", 
                        text="匯率查詢"
                    ), 
                ]
                )
        )
    
    return button_template
