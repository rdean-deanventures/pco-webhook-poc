from flask import Flask, request, jsonify
from processor import process_webhook

app = Flask(__name__)

@app.route("/")
def home():
    return "Planning Center Webhook POC is running!"

@app.route("/webhook", methods=["POST"])
def webhook():

    payload = request.get_json()

    print("\n==============================")
    print("WEBHOOK RECEIVED")
    print("==============================")

    print(payload)

    # Send to processor
    process_webhook(payload)

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    app.run(debug=True)