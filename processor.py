import json


def process_webhook(payload):

    print("\n=================================")
    print("PROCESSOR STARTED")
    print("=================================")

    print(f"Payload Type: {type(payload)}")

    try:
        print("\nFULL PAYLOAD:")
        print(json.dumps(payload, indent=4))
    except Exception as e:
        print(f"Could not format JSON: {e}")
        print(payload)

    print("\n=================================")
    print("PROCESSOR COMPLETE")
    print("=================================\n")

