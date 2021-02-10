import telnyx
from flask import Flask, request, Response
from dotenv import load_dotenv
load_dotenv()
import os
import json
from urllib.parse import urlunsplit

app = Flask(__name__)

@app.route("/status", methods=['POST'])
def outbound_status():
    body        = json.loads(request.data)
    payload     = body["data"]["payload"]
    message_id  = payload["id"]
    status      = payload["to"][0]["status"]
    print(f"Delivery status: {status}")
    return Response(status=200)

def send_sms(from_number, to_number, text):
    webhook_url = urlunsplit((
        request.scheme,
        request.host,
        "/status",
        "", ""))
    telnyx_request = {
        "from_": to_number,
        "to" : from_number,
        "webhook_url": webhook_url,
        "use_profile_webhooks": False,
        "text": text
    }
    try:
        telnyx_response = telnyx.Message.create(**telnyx_request)
        print(f"Sent message with ID: {telnyx_response.id}")
    except Exception as e:
        print("Error sending message")
        print(e)

def get_response(text):
    responses = {
        "pizza": "Chicago has the best pizza.",
        "ice cream": "I prefer gelato.",
    }
    for keyword, reply in responses.items():
        if keyword.lower() in text:
            return reply
    return "Please text the word 'pizza' or 'ice cream' for a different response."

@app.route("/webhooks", methods=['POST'])
def inbound_sms():
    body        = json.loads(request.data)
    payload     = body["data"]["payload"]
    message_id  = payload["id"]
    to_number   = payload["to"][0]["phone_number"]
    from_number = payload["from"]["phone_number"]
    text        = payload["text"].strip().lower()
    print(f"Received message with ID: {message_id}")
    response = get_response(text)
    send_sms(from_number, to_number, response)
    return Response(status=200)

if __name__ == "__main__":
    telnyx.api_key = os.getenv("TELNYX_API_KEY")
    telnyx.public_key = os.getenv("TELNYX_PUBLIC_KEY")
    TELNYX_APP_PORT = os.getenv("PORT")
    app.run(port=TELNYX_APP_PORT)