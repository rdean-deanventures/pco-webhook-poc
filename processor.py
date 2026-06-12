import json
import requests

# -------------------------------------
# EMAILJS SETTINGS
# -------------------------------------
SERVICE_ID = "service_cdqifd9"
TEMPLATE_ID = "template_e632ic2"
PUBLIC_KEY = "D3PHlEkPv4MmvSxz1"
PRIVATE_KEY = "Ii-i6oKAS2Gz0D2yagQIj"


def process_webhook(payload):

    print("\n=================================")
    print("PROCESSOR STARTED")
    print("=================================")

    try:

        # Get first event from webhook delivery
        event = payload["data"][0]

        event_name = event["attributes"]["name"]

        print(f"Event Name: {event_name}")

        # Planning Center sends the actual event payload as a JSON string
        raw_event_payload = event["attributes"]["payload"]

        # Convert JSON string into Python dictionary
        event_payload = json.loads(raw_event_payload)

        person_data = event_payload["data"]

        person_id = person_data["id"]

        person_attributes = person_data["attributes"]

        full_name = person_attributes.get("name", "")

        print(f"Person ID: {person_id}")
        print(f"Person Name: {full_name}")

        # -------------------------------------
        # SIMPLE EMAIL TEST
        # -------------------------------------
        send_test_email()

    except Exception as e:

        print("ERROR IN PROCESSOR:")
        print(str(e))

    print("=================================")
    print("PROCESSOR COMPLETE")
    print("=================================\n")


def send_test_email():

    print("ATTEMPTING EMAIL SEND...")

    payload = {
        "service_id": SERVICE_ID,
        "template_id": TEMPLATE_ID,
        "user_id": PUBLIC_KEY,
        "accessToken": PRIVATE_KEY,
        "template_params": {
            "message": "Webhook received successfully."
        }
    }

    try:

        response = requests.post(
            "https://api.emailjs.com/api/v1.0/email/send",
            json=payload
        )

        print("EMAILJS STATUS:", response.status_code)
        print("EMAILJS RESPONSE:", response.text)

    except Exception as e:

        print("EMAIL SEND FAILED:")
        print(str(e))