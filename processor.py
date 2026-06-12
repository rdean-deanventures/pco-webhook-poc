from datetime import datetime

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
