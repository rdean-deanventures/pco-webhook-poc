from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Planning Center Webhook POC is running!"

@app.route("/webhook", methods=["POST"])
def webhook():

    print("\n==============================")
    print("PLANNING CENTER WEBHOOK RECEIVED")
    print(datetime.now())
    print("==============================")

    # Get raw JSON payload
    payload = request.get_json()

    # Print full payload in Render logs
    print(json.dumps(payload, indent=2))

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    app.run(debug=True)