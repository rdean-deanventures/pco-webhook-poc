from datetime import datetime

import requests


def handle_webhook_event(payload):
    """
    This is your main webhook processor.
    Right now it's just a proof of concept.
    """

    print("\n===== PROCESSOR TRIGGERED =====")
    print("Time:", datetime.now())

    # Print the payload received from Planning Center
    print("Payload received:")
    print(payload)

    print("===== END PROCESSOR =====\n")




EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

SERVICE_ID = "service_cdqifd9"
TEMPLATE_ID = "template_e632ic2"
PUBLIC_KEY = "D3PHlEkPv4MmvSxz1"

def send_email(payload):

    name = payload.get("data", {}).get("attributes", {}).get("name", "Unknown")
    person_id = payload.get("data", {}).get("id", "Unknown")

    data = {
        "service_id": SERVICE_ID,
        "template_id": TEMPLATE_ID,
        "user_id": PUBLIC_KEY,
        "template_params": {
            "name": name,
            "id": person_id,
            "payload": str(payload)
        }
    }

    response = requests.post(EMAILJS_URL, json=data)

    print("EMAILJS RESPONSE:", response.status_code, response.text)


