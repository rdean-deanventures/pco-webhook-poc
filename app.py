from flask import Flask, request, jsonify
import json

from processor import handle_webhook_event

app = Flask(__name__)

@app.route("/")
def home():
    return "Planning Center Webhook POC is running!"

@app.route("/webhook", methods=["POST"])
def webhook():

    payload = request.get_json()

    print("\n==============================")
    print("WEBHOOK RECEIVED IN FLASK")
    print("==============================")

    print(json.dumps(payload, indent=2))

    # 👇 THIS is the key change
    handle_webhook_event(payload)

    return jsonify({"status": "processed"}), 200


if __name__ == "__main__":
    app.run(debug=True)