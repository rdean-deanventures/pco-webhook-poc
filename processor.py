import requests

# -----------------------------
# EMAILJS CONFIG
# -----------------------------
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

SERVICE_ID = "YOUR_SERVICE_ID"
TEMPLATE_ID = "YOUR_TEMPLATE_ID"
PUBLIC_KEY = "YOUR_PUBLIC_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"


def process_webhook(payload):

    print("\n==============================")
    print("PROCESSOR STARTED")
    print("==============================")

    try:
        # -----------------------------------
        # HANDLE LIST OR DICT PAYLOAD SAFELY
        # -----------------------------------
        if isinstance(payload, list):
            event = payload[0]
        else:
            event = payload

        print("RAW EVENT:")
        print(event)

        # -----------------------------------
        # EXTRACT DATA SAFELY
        # -----------------------------------
        data = event.get("data", {})
        attributes = data.get("attributes", {})

        # Planning Center People usually split names
        first_name = attributes.get("first_name", "")
        last_name = attributes.get("last_name", "")
        full_name = attributes.get("name")

        # Fallback logic
        if full_name:
            name = full_name
        else:
            name = f"{first_name} {last_name}".strip()

        person_id = data.get("id", "Unknown")

        print(f"Person Name: {name}")
        print(f"Person ID: {person_id}")

        # -----------------------------------
        # SEND EMAIL
        # -----------------------------------
        send_email(name, person_id, event)

    except Exception as e:
        print("ERROR IN PROCESSOR:")
        print(str(e))
        print("FULL PAYLOAD:")
        print(payload)

    print("==============================")
    print("PROCESSOR COMPLETE")
    print("==============================\n")


def send_email(name, person_id, payload):

    print("SENDING EMAIL VIA EMAILJS...")

    data = {
        "service_id": SERVICE_ID,
        "template_id": TEMPLATE_ID,
        "user_id": PUBLIC_KEY,
        "accessToken": PRIVATE_KEY,
        "template_params": {
            "name": name,
            "id": person_id,
            "payload": str(payload)
        }
    }

    try:
        response = requests.post(EMAILJS_URL, json=data)

        print("EMAILJS STATUS:", response.status_code)
        print("EMAILJS RESPONSE:", response.text)

    except Exception as e:
        print("EMAIL FAILED:")
        print(str(e))


