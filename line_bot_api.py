from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler, exceptions
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

line_bot_api = LineBotApi("bobQ6mg/o0rZkBrYzuZ/DUKC3GrbqDqjMwf88EAjgbWqgGDejIRauFUMCiLC2gBGhQ5IhJSZSnNVEzsVUrln9VOk9DujR1v6zyCSXxvlBwUlhfNo7s6HyZH6Z0v2SCbHzC4OGtenkr+Tu+JSS6xDkAdB04t89/1O/w1cDnyilFU=")

handler = WebhookHandler("278f2f753e15266cf1b77462929c3f4a")