from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Planning Center Webhook POC is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    print("Webhook received!")
    return {"status": "success"}

if __name__ == "__main__":
    app.run(debug=True)