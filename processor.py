import json


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

        first_name = person_attributes.get("first_name", "")
        last_name = person_attributes.get("last_name", "")
        full_name = person_attributes.get("name", "")

        print(f"Person ID: {person_id}")
        print(f"Person Name: {full_name}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")

    except Exception as e:

        print("ERROR IN PROCESSOR:")
        print(str(e))

    print("=================================")
    print("PROCESSOR COMPLETE")
    print("=================================\n")