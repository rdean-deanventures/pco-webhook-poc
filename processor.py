import requests

# -----------------------------
# EMAILJS CONFIG (REPLACE THESE)
# -----------------------------
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

SERVICE_ID = "service_cdqifd9"
TEMPLATE_ID = "template_e632ic2"
PUBLIC_KEY = "D3PHlEkPv4MmvSxz1"


def process_webhook(payload):
    """
    Main processor for Planning Center webhook events
    """

    print("\n===== PROCESSOR STARTED =====")

    # Extract safe fields from Planning Center payload
    try:
        person = payload.get("data", {})
        attributes = person.get("attributes", {})

        name = attributes.get("name", "Unknown")
        person_id = person.get("id", "Unknown")

        print(f"Person Name: {name}")
        print(f"Person ID: {person_id}")

    except Exception as e:
        print("Error parsing payload:", e)
        name = "Unknown"
        person_id = "Unknown"

    # Send email
    send_email(name, person_id, payload)

    print("===== PROCESSOR COMPLETE =====\n")


def send_email(name, person_id, payload):

    print("SENDING EMAIL VIA EMAILJS...")

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

    try:
        response = requests.post(EMAILJS_URL, json=data)

        print("EMAILJS STATUS:", response.status_code)
        print("EMAILJS RESPONSE:", response.text)

    except Exception as e:
        print("EMAIL SEND FAILED:", str(e))


