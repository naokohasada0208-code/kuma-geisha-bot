from flask import Flask, request
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "ここにLINEのトークン"

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/callback", methods=['POST'])
def callback():
    data = request.json

    for event in data["events"]:
        if event["type"] == "message":
            reply_token = event["replyToken"]
            user_message = event["message"]["text"]

            reply(reply_token, user_message)

    return "OK"

def reply(reply_token, text):
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    body = {B8kSk1g16sdOh2H45fmhbDndoHLobhL885v8SVGa4fDD9tgUNV4cAVHqSuV1O683N/l7YEE5vQUsndV8ulDyZpDZ1SNtV28ugxTj8Ta+O+Tl5+OuhJuQKb98Qn35qtoNv4qf3J8d+aJNHAJc46VaSAdB04t89/1O/w1cDnyilFU=        "replyToken": reply_token,
        "messages": [
            {"type": "text", "text": f"あなたのメッセージ: {text}"}
        ]
    }

    requests.post(url, headers=headers, json=body)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
